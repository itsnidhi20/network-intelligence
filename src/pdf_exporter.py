from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(report, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Investigation Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"<b>Entity:</b> {report['Entity']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Risk Score:</b> {report['Risk Score']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Risk Level:</b> {report['Risk Level']}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Reasons</b>",
            styles["Heading2"]
        )
    )

    for reason in report["Reasons"]:

        content.append(
            Paragraph(
                f"• {reason}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Recommendation</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            report["Recommendation"],
            styles["BodyText"]
        )
    )

    doc.build(content)