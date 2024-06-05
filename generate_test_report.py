import json
import os
from datetime import datetime

def parse_test_results():
    with open('test-results.json', 'r') as file:
        return json.load(file)

def generate_report(test_results):
    report = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Results Report</title>
    <link rel="stylesheet" href="report_style.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
        }
        h1, h2, h3 {
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
        .suite {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .passed {
            color: green;
        }
        .failed {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Test Results Report</h1>
        <h2>Summary</h2>
        <ul>
    """

    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    duration = test_results['stats']['duration']

    for suite in test_results['suites']:
        for subsuite in suite['suites']:
            for nested_suite in subsuite['suites']:
                total_tests += len(nested_suite['specs'])
                for spec in nested_suite['specs']:
                    for test in spec['tests']:
                        if test['results'][0]['status'] == 'passed':
                            passed_tests += 1
                        else:
                            failed_tests += 1

    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    report += f"""
        <li><strong>Date:</strong> {date_str}</li>
        <li><strong>Total Tests:</strong> {total_tests}</li>
        <li><strong>Passed:</strong> {passed_tests}</li>
        <li><strong>Failed:</strong> {failed_tests}</li>
        <li><strong>Duration:</strong> {duration} ms</li>
    """

    report += """
        </ul>
        <h2>Test Details</h2>
    """

    for suite in test_results['suites']:
        for subsuite in suite['suites']:
            report += f"""
                <div class="suite">
                    <h3>{subsuite['title']}</h3>
                    <ul>
            """
            for nested_suite in subsuite['suites']:
                report += f"<h4>{nested_suite['title']}</h4>"
                for spec in nested_suite['specs']:
                    result_class = 'passed' if spec['tests'][0]['results'][0]['status'] == 'passed' else 'failed'
                    report += f"""
                        <li class="{result_class}">
                            <strong>Test:</strong> {spec['title']}<br>
                            <strong>Status:</strong> {spec['tests'][0]['results'][0]['status']}<br>
                            <strong>Duration:</strong> {spec['tests'][0]['results'][0]['duration']} ms<br>
                            <strong>Errors:</strong> {', '.join([error['message'] for error in spec['tests'][0]['results'][0]['errors']]) if spec['tests'][0]['results'][0]['errors'] else 'None'}
                        </li>
                    """
            report += """
                    </ul>
                </div>
            """

    report += """
    </div>
</body>
</html>
    """
    return report

def main():
    os.system('npx playwright test --reporter=json > test-results.json')

    test_results = parse_test_results()
    report = generate_report(test_results)

    with open('test_results_report.html', 'w') as file:
        file.write(report)

    print("Test results report generated and saved to 'test_results_report.html'")

if __name__ == "__main__":
    main()