import os
from rest_framework import serializers
from django.conf import settings

from .models import Assessment, Answer
from .questions_config import QUESTIONS
from .pdf_report import generate_pdf_report
from .scoring import (
    compute_raw_percentage_from_numeric_scores,
    apply_capping,
    get_category,
)
from .feedback import generate_narrative


# Fast lookup
QUESTION_INDEX = {q["id"]: q for q in QUESTIONS}
RATED_QUESTIONS = [f"Q{i}" for i in range(1, 16)]


class AssessmentCreateSerializer(serializers.Serializer):
    # -----------------------------
    # Contact Details
    # -----------------------------
    person_name = serializers.CharField(required=False, allow_blank=True)
    company_name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField()
    phone = serializers.CharField(required=False, allow_blank=True)
    designation = serializers.CharField(required=False, allow_blank=True)

    # -----------------------------
    # Business Info
    # -----------------------------
    industry = serializers.CharField(required=False, allow_blank=True)
    prioritized_use_case = serializers.CharField(required=False, allow_blank=True)
    automation_areas = serializers.ListField(
        child=serializers.CharField(), required=False
    )
    automation_areas_other = serializers.CharField(required=False, allow_blank=True)

    # -----------------------------
    # Answers Payload
    # -----------------------------
    answers = serializers.DictField()

    # -----------------------------
    # Validation
    # -----------------------------
    def validate(self, data):
        answers = data.get("answers", {})

        # Ensure all rated questions exist
        missing = [q for q in RATED_QUESTIONS if q not in answers]
        if missing:
            raise serializers.ValidationError(
                {"answers": f"Missing required questions: {missing}"}
            )

        # Validate rated questions (single choice 1–5 mapped via options)
        for qid in RATED_QUESTIONS:
            config = QUESTION_INDEX.get(qid)
            if not config:
                raise serializers.ValidationError({qid: "Invalid question ID"})

            if answers[qid] not in config["options"]:
                raise serializers.ValidationError(
                    {qid: f"Invalid option. Allowed: {config['options']}"}
                )

        return data

    # -----------------------------
    # Create Assessment
    # -----------------------------
    def create(self, validated_data):
        answers = validated_data["answers"]

        # Create Assessment
        assessment = Assessment.objects.create(
            person_name=validated_data.get("person_name"),
            company_name=validated_data.get("company_name"),
            email=validated_data["email"],
            phone=validated_data.get("phone"),
            designation=validated_data.get("designation"),
            industry=validated_data.get("industry") or answers.get("INDUSTRY"),
            prioritized_use_case=validated_data.get("prioritized_use_case")
            or answers.get("USE_CASE"),
            automation_areas=validated_data.get("automation_areas")
            or answers.get("AUTOMATION_AREAS"),
            automation_areas_other=validated_data.get("automation_areas_other"),
        )

        # -----------------------------
        # Save Answers + Numeric Scores
        # -----------------------------
        numeric_scores = {}

        for qid in RATED_QUESTIONS:
            config = QUESTION_INDEX[qid]
            selected_option = answers[qid]

            # Map option → numeric score (1–5)
            numeric_value = config["options"].index(selected_option) + 1

            Answer.objects.create(
                assessment=assessment,
                question_id=qid,
                question_text=config["label"],
                numeric_value=numeric_value,
                raw_value=selected_option,
            )

            numeric_scores[qid] = numeric_value

        # Save non-scored answers (traceability)
        for qid, value in answers.items():
            if qid in RATED_QUESTIONS:
                continue

            qmeta = QUESTION_INDEX.get(qid)
            Answer.objects.create(
                assessment=assessment,
                question_id=qid,
                question_text=qmeta["label"] if qmeta else qid,
                raw_value=value,
            )

        # -----------------------------
        # Scoring Logic
        # -----------------------------
        raw_pct = compute_raw_percentage_from_numeric_scores(numeric_scores)
        capped_pct = apply_capping(raw_pct)
        category = get_category(capped_pct)
        narrative = generate_narrative(assessment, raw_pct, capped_pct)

        assessment.raw_score = raw_pct
        assessment.capped_score = capped_pct
        assessment.category = category
        assessment.narrative = narrative
        assessment.save()

        # -----------------------------
        # AUTO-GENERATE PDF (🔥 KEY FIX)
        # -----------------------------
        # reports_dir = os.path.join(settings.MEDIA_ROOT, "reports")
        # os.makedirs(reports_dir, exist_ok=True)

        # filename = f"{assessment.id}.pdf"
        # pdf_path = os.path.join(reports_dir, filename)

        # generate_pdf_report(assessment, pdf_path)

        # assessment.pdf_report_path = f"{settings.MEDIA_URL}reports/{filename}"
        # assessment.save(update_fields=["pdf_report_path"])

        return assessment


# -----------------------------
# Read-Only Serializers
# -----------------------------
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["question_id", "question_text", "numeric_value", "raw_value"]


class AssessmentDetailSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = [
            "id",
            "person_name",
            "company_name",
            "email",
            "phone",
            "designation",
            "industry",
            "prioritized_use_case",
            "automation_areas",
            "automation_areas_other",
            "raw_score",
            "capped_score",
            "category",
            "narrative",
            "pdf_report_path",
            "created_at",
            "answers",
        ]
