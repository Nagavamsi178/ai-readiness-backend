from django.urls import path
from .views import QuestionsView, SubmitAssessmentView, AssessmentDetailView, PDFReportView

urlpatterns = [
    path("questions/", QuestionsView.as_view()),
    path("submit/", SubmitAssessmentView.as_view()),
    path("assessments/<uuid:id>/", AssessmentDetailView.as_view()),
    path("report/<uuid:id>/", PDFReportView.as_view(), name="ai-readiness-report"),
]
