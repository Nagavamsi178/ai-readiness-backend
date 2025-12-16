from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Assessment, Answer


# -----------------------------
# Inline Answer Table (Read-only)
# -----------------------------
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ("question_id", "question_text",
                       "numeric_value", "raw_value")
    can_delete = False
    show_change_link = False


# -----------------------------
# Assessment Admin Panel
# -----------------------------
@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "company_name",
        "capped_score",
        "category",
        "pdf_link",        # ✅ Clickable PDF link
        "created_at",
    )

    search_fields = ("email", "company_name", "person_name")
    list_filter = ("category", "industry", "created_at")

    readonly_fields = (
        "raw_score",
        "capped_score",
        "category",
        "narrative",
        "pdf_report_path",
        "pdf_link",        # ✅ visible in detail view
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Client Contact Info", {
            "fields": (
                "person_name",
                "company_name",
                "email",
                "phone",
                "designation",
            )
        }),

        ("Business & Use Case", {
            "fields": (
                "industry",
                "prioritized_use_case",
                "automation_areas",
                "automation_areas_other",
            )
        }),

        ("Assessment Scoring", {
            "fields": (
                "raw_score",
                "capped_score",
                "category",
            )
        }),

        ("Narrative Summary", {
            "fields": ("narrative",)
        }),

        ("PDF Report", {
            "fields": ("pdf_link",)
        }),

        ("System Info", {
            "fields": ("created_at", "updated_at")
        }),
    )

    inlines = [AnswerInline]

    # -----------------------------
    # PDF Link (On-demand generation)
    # -----------------------------
    def pdf_link(self, obj):
        if not obj.id:
            return "-"

        url = reverse(
            "ai-readiness-report",   # URL name from urls.py
            kwargs={"id": obj.id}
        )

        return format_html(
            '<a href="{}" target="_blank" style="font-weight:600;">📄 View PDF</a>',
            url
        )

    pdf_link.short_description = "PDF Report"
    pdf_link.allow_tags = True


# -----------------------------
# Answer Admin Panel (Optional)
# -----------------------------
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("assessment", "question_id", "numeric_value", "created_at")
    search_fields = ("assessment__email", "question_id", "question_text")
    list_filter = ("question_id",)
    readonly_fields = (
        "assessment",
        "question_id",
        "question_text",
        "numeric_value",
        "raw_value",
        "created_at",
    )
