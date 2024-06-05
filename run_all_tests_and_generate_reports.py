import subprocess
import os
import webbrowser
import time

def run_script(script_name):
    try:
        subprocess.run(['python3', script_name], check=True)
        print(f"Successfully ran {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        return False
    return True

def run_playwright_tests():
    try:
        subprocess.run(['npx', 'playwright', 'test'], check=True)
        print("Successfully ran Playwright tests")
    except subprocess.CalledProcessError as e:
        print(f"Error running Playwright tests: {e}")
        return False
    return True

def find_new_html_files():
    current_files = set(os.listdir('.'))
    html_files = [file for file in current_files if file.endswith('.html')]
    return html_files

def main():
    initial_html_files = find_new_html_files()

    # Run compare_html.py
    if not run_script('compare_html.py'):
        return

    # Run Playwright tests
    if not run_playwright_tests():
        return

    # Run generate*report.py files
    for script_name in os.listdir('.'):
        if script_name.startswith('generate') and script_name.endswith('report.py'):
            if not run_script(script_name):
                return

    # Find new HTML files created
    final_html_files = find_new_html_files()
    new_html_files = set(final_html_files) - set(initial_html_files)

    print("New HTML files created:")
    for html_file in new_html_files:
        print(html_file)

    # Open the test results report in the default browser if it exists
    report_file = 'test_results_report.html'
    report_path = os.path.abspath(report_file)
    print(f"Looking for file: {report_path}")

    if os.path.exists(report_path):
        print(f"Opening file: {report_path}")
        webbrowser.open(f"file://{report_path}")
    else:
        print(f"File {report_path} does not exist.")

if __name__ == "__main__":
    main()