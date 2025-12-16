import uuid
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe


class Assessment(models.Model):
    """
    Stores one full assessment submission with contact info, business details,
    scoring, narrative, and PDF report reference.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Contact / Lead Info
    person_name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)

    # Industry & Prioritized Use Case
    industry = models.CharField(max_length=255, blank=True, null=True)
    prioritized_use_case = models.TextField(blank=True, null=True)

    # Automation Areas (Multi-Select JSON List)
    automation_areas = models.JSONField(blank=True, null=True)  # e.g. ["Finance", "HR", "IT"]
    automation_areas_other = models.TextField(blank=True, null=True)

    # Scoring
    raw_score = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)     # 0–100% raw
    capped_score = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # after capping rule
    category = models.CharField(max_length=50, blank=True, null=True)  # AI Aspirant / Explorer / Adopter

    # Optional dimension-wise breakdown
    dimension_scores = models.JSONField(blank=True, null=True)

    # Narrative summary to show in PDF or UI
    narrative = models.TextField(blank=True, null=True)

    # PDF file URL or path
    pdf_report_path = models.CharField(max_length=512, blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company_name or self.email} ({self.capped_score or 'Pending'}%)"

    # 🔗 Clickable PDF link for Admin panel
    def pdf_link(self):
        if self.pdf_report_path:
            return mark_safe(f'<a href="{self.pdf_report_path}" target="_blank">📄 Download PDF</a>')
        return "No PDF"

    pdf_link.short_description = "PDF Report"


class Answer(models.Model):
    """
    Stores each answer for Q1–Q15 (integer 1–5),
    plus additional text or multi-choice values.
    """
    assessment = models.ForeignKey(
        Assessment, on_delete=models.CASCADE, related_name="answers"
    )
    question_id = models.CharField(max_length=10)  # Q1..Q15 or custom
    question_text = models.TextField()

    # Rated questions store numeric values (1–5)
    numeric_value = models.IntegerField(null=True, blank=True)

    # Other fields store JSON or text (multi-choice, comments etc.)
    raw_value = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("assessment", "question_id")

    def __str__(self):
        return f"{self.assessment.email} - {self.question_id}"
