def create_text_report(report):

    content = ""

    content += f"Entity: {report['Entity']}\n"
    content += f"Risk Score: {report['Risk Score']}\n"
    content += f"Risk Level: {report['Risk Level']}\n\n"

    content += "Connections:\n"

    for connection in report["Connections"]:
        content += f"- {connection}\n"

    content += "\nCommunity:\n"

    for member in report["Community"]:
        content += f"- {member}\n"

    content += "\nReasons:\n"

    for reason in report["Reasons"]:
        content += f"- {reason}\n"

    content += "\nRecommendation:\n"
    content += report["Recommendation"]

    return content