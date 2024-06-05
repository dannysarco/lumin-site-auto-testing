import difflib
from bs4 import BeautifulSoup
from datetime import datetime

def extract_elements(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = []

    for element in soup.find_all(True):
        text = element.get_text(strip=True)
        attributes = element.attrs
        # Convert list attribute values to tuples for hashing
        attributes = {k: tuple(v) if isinstance(v, list) else v for k, v in attributes.items()}
        elements.append({
            'tag': element.name,
            'text': text,
            'attributes': attributes
        })

    return elements

def compare_elements(old_elements, new_elements):
    old_set = {(el['tag'], el['text'], frozenset(el['attributes'].items())) for el in old_elements}
    new_set = {(el['tag'], el['text'], frozenset(el['attributes'].items())) for el in new_elements}

    added_elements = new_set - old_set
    removed_elements = old_set - new_set

    return list(added_elements), list(removed_elements)

def generate_report(added_elements, removed_elements):
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    report = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LuminSmart Homepage Diff Report</title>
    <link rel="stylesheet" href="report_style.css">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
        }}
        h1, h2 {{
            text-align: center;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin: 5px 0;
        }}
        .added {{
            color: green;
        }}
        .removed {{
            color: red;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>LuminSmart Homepage Diff Report</h1>
        <h2>Report Summary</h2>
        <ul>
            <li><strong>Date:</strong> {date_str}</li>
            <li><strong>Added Elements:</strong> {len(added_elements)}</li>
            <li><strong>Removed Elements:</strong> {len(removed_elements)}</li>
        </ul>
        <h2>Added Elements (First 10)</h2>
        <ul class="added">
    """

    for i, element in enumerate(added_elements[:10]):
        tag, text, attributes = element
        report += f"""
            <li>
                <strong>Element:</strong> {tag}<br>
                <strong>Text:</strong> {text}<br>
                <strong>Attributes:</strong> {dict(attributes)}
            </li>
        """

    report += """
        </ul>
        <h2>Removed Elements (First 10)</h2>
        <ul class="removed">
    """

    for i, element in enumerate(removed_elements[:10]):
        tag, text, attributes = element
        report += f"""
            <li>
                <strong>Element:</strong> {tag}<br>
                <strong>Text:</strong> {text}<br>
                <strong>Attributes:</strong> {dict(attributes)}
            </li>
        """

    report += """
        </ul>
    </div>
</body>
</html>
    """
    return report

def main():
    with open('luminsmart_homepage_previous.html', 'r') as file:
        old_html_content = file.read()

    with open('luminsmart_homepage.html', 'r') as file:
        new_html_content = file.read()

    old_elements = extract_elements(old_html_content)
    new_elements = extract_elements(new_html_content)

    added_elements, removed_elements = compare_elements(old_elements, new_elements)

    report = generate_report(added_elements, removed_elements)

    with open('luminsmart_homepage_diff_report.html', 'w') as file:
        file.write(report)

    print("Report generated and saved to 'luminsmart_homepage_diff_report.html'")

if __name__ == "__main__":
    main()