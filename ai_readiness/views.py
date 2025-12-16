from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import FileResponse, Http404
from .questions_config import QUESTIONS
from .serializers import AssessmentCreateSerializer, AssessmentDetailSerializer
from .models import Assessment
from .pdf_report import generate_pdf_report
import os
import io
from django.conf import settings


class QuestionsView(APIView):
    def get(self, request):
        return Response({"questions": QUESTIONS})


class SubmitAssessmentView(APIView):
    def post(self, request):
        serializer = AssessmentCreateSerializer(data=request.data)
        if serializer.is_valid():
            assessment = serializer.save()
            out = AssessmentDetailSerializer(assessment)
            return Response(out.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssessmentDetailView(generics.RetrieveAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentDetailSerializer
    lookup_field = "id"


# class PDFReportView(APIView):
#     def get(self, request, id):
#         try:
#             assessment = Assessment.objects.get(id=id)
#         except Assessment.DoesNotExist:
#             raise Http404("Assessment not found")

#         if not assessment.pdf_report_path:
#             raise Http404("PDF not available")

#         pdf_path = os.path.join(
#             settings.MEDIA_ROOT,
#             assessment.pdf_report_path.replace(
#                 settings.MEDIA_URL, "").lstrip("/")
#         )

#         return FileResponse(
#             open(pdf_path, "rb"),
#             content_type="application/pdf",
#             filename=f"{assessment.id}.pdf",
#         )

class PDFReportView(APIView):
    def get(self, request, id):
        try:
            assessment = Assessment.objects.get(id=id)
        except Assessment.DoesNotExist:
            raise Http404("Assessment not found")

        # Request-level cache
        if not hasattr(request, "_cached_pdf"):
            buffer = io.BytesIO()
            generate_pdf_report(assessment, buffer)
            buffer.seek(0)
            request._cached_pdf = buffer

        return FileResponse(
            request._cached_pdf,
            as_attachment=True,
            filename=f"AI_Readiness_Report_{assessment.id}.pdf",
            content_type="application/pdf",
        )