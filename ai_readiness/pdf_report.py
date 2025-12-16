from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
import math
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from textwrap import wrap


def draw_doughnut(c, x, y, size, percent):
    """
    Draws a real doughnut chart using ReportLab Pie.
    percent: 0–100
    """
    drawing = Drawing(size, size)

    pie = Pie()
    pie.x = 0
    pie.y = 0
    pie.width = size
    pie.height = size

    pie.data = [percent, 100 - percent]
    pie.startAngle = 90

    pie.slices[0].fillColor = colors.HexColor("#22c55e")  # green
    pie.slices[1].fillColor = colors.lightgrey
    pie.slices[0].strokeWidth = 0
    pie.slices[1].strokeWidth = 0

    # Create doughnut hole
    pie.innerRadiusFraction = 0.6

    drawing.add(pie)
    drawing.drawOn(c, x, y)

    # Percentage label
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.black)
    c.drawCentredString(
        x + size / 2,
        y + size / 2 - 8,
        f"{int(percent)}%"
    )


def draw_wrapped_text(c, text, x, y, max_width, leading=14):
    """
    Draw wrapped paragraph text within a fixed width.
    """
    text_obj = c.beginText(x, y)
    text_obj.setLeading(leading)
    text_obj.setFont("Helvetica", 10)

    # Approx chars per line (ReportLab has no auto wrap)
    max_chars = int(max_width / 6)

    for line in text.splitlines():
        wrapped_lines = wrap(line, max_chars) or [""]
        for wline in wrapped_lines:
            text_obj.textLine(wline)

    c.drawText(text_obj)
    return y - (len(text.splitlines()) * leading)


def generate_pdf_report(assessment, output):
    # c = canvas.Canvas(file_path, pagesize=A4)
    c = canvas.Canvas(output, pagesize=A4)
    width, height = A4

    LEFT_MARGIN = 40
    RIGHT_MARGIN = 40
    TOP_MARGIN = height - 50

    CONTENT_WIDTH = width - LEFT_MARGIN - RIGHT_MARGIN
    LEFT_COL_WIDTH = 320     # text column
    RIGHT_COL_X = LEFT_MARGIN + LEFT_COL_WIDTH + 20  # chart column

    # header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(LEFT_MARGIN, TOP_MARGIN, "AI Readiness Report — Forgebyte")

    # client info
    c.setFont("Helvetica", 11)
    lines = [
        f"Name: {assessment.person_name or ''}",
        f"Company: {assessment.company_name or ''}",
        f"Email: {assessment.email}",
        f"Phone: {assessment.phone or ''}",
        f"Designation: {assessment.designation or ''}",
        f"Industry: {assessment.industry or ''}",
    ]

    y = TOP_MARGIN - 30
    for ln in lines:
        c.drawString(LEFT_MARGIN, y, ln)
        y -= 14

    # draw doughnut (right column)
    pct = float(assessment.capped_score or 0)
    draw_doughnut(
        c,
        x=RIGHT_COL_X,
        y=TOP_MARGIN - 200,
        size=140,
        percent=pct,
    )

    # summary title
    c.setFont("Helvetica-Bold", 12)
    c.drawString(LEFT_MARGIN, y - 10, "Summary")

    # summary text (wrapped, left column only)
    narrative_text = assessment.narrative or ""
    draw_wrapped_text(
        c,
        narrative_text,
        x=LEFT_MARGIN,
        y=y - 30,
        max_width=LEFT_COL_WIDTH,
        leading=14,
    )

    # answers on next page
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawString(LEFT_MARGIN, height - 50, "Client Responses (Raw Answers)")

    y = height - 80
    c.setFont("Helvetica", 10)

    for ans in assessment.answers.all():
        if y < 80:
            c.showPage()
            y = height - 60
            c.setFont("Helvetica", 10)

        qline = f"{ans.question_id}: {ans.question_text}"
        draw_wrapped_text(
            c,
            qline,
            x=LEFT_MARGIN,
            y=y,
            max_width=CONTENT_WIDTH,
            leading=12,
        )
        y -= 14

        if ans.numeric_value is not None:
            answer_text = f"Answer (1–5): {ans.numeric_value}"
        elif ans.raw_value:
            answer_text = f"Answer: {ans.raw_value}"
        else:
            answer_text = "Answer: -"

        draw_wrapped_text(
            c,
            answer_text,
            x=LEFT_MARGIN + 20,
            y=y,
            max_width=CONTENT_WIDTH - 20,
            leading=12,
        )

        y -= 22

    c.save()
    # return file_path
