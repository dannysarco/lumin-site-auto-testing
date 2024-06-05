# LuminSmart Automated Testing 🎉

This repository contains automated tests for the LuminSmart website. The tests are designed to ensure that the website's UI elements function correctly and to detect any changes in the HTML structure of the homepage. The tests are written using Playwright and Python.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Generating Reports](#generating-reports)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.7+
- Node.js and npm
- Playwright

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/dannysarco/lumin-site-auto-testing.git
    cd lumin-site-auto-testing
    ```
2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. Install the Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Install Playwright and its dependencies:
    ```sh
    npm install
    npx playwright install
    ```

## Running the Tests
To run all the tests and generate the reports, execute the following command:
```sh
python3 run_all_tests_and_generate_reports.py
```
This script will:
1. Run the `compare_html.py` script to compare the current HTML structure of the LuminSmart homepage with a previous version.
2. Run all Playwright tests defined in any `*.spec.js` files.
3. Generate HTML reports using `generate_test_report.py` and `generate_diff_report.py`.

If everything runs successfully, the script will open the `test_results_report.html` file in your default web browser.

## Generating Reports
The project includes scripts to generate detailed HTML reports:
- **Test Results Report**: Summarizes the results of the Playwright tests.
- **HTML Diff Report**: Highlights the differences between the current and previous versions of the LuminSmart homepage HTML.

These reports are generated automatically when you run `run_all_tests_and_generate_reports.py`.

## Development Guidelines

Please follow the development guidelines to ensure consistency and maintainability:
- [Branch Naming Guidelines](https://github.com/dannysarco/lumin-site-auto-testing/blob/main/development-guidelines/BRANCH_NAMING_GUIDELINES)
- [Merging Guidelines](https://github.com/dannysarco/lumin-site-auto-testing/blob/main/development-guidelines/MERGING_GUIDELINES)

## Project Structure
```plaintext
lumin-site-auto-testing/
├── .github/
│   └── PR_TEMPLATE.md
├── development-guidelines/
│   ├── BRANCH_NAMING_GUIDELINES.md
│   └── MERGING_GUIDELINES.md
├── scripts/
│   ├── compare_html.py
│   ├── generate_diff_report.py
│   ├── generate_test_report.py
│   ├── run_all_tests_and_generate_reports.py
│   └── extract_elements.py
├── tests/
│   └── homepage.spec.js
├── .gitignore
├── README.md
└── requirements.txt
```
- **extract-elements.py**: Script to extract HTML elements for comparison.
- **generate_diff_report.py**: Generates a report highlighting differences in HTML structure.
- **generate_test_report.py**: Generates a detailed report of the test results.
- **homepage.spec.js**: Playwright tests for the LuminSmart homepage.
- **run_all_tests_and_generate_reports.py**: Main script to run all tests and generate reports.
- **compare_html.py**: Script to compare the current and previous versions of the LuminSmart homepage HTML.
- **tests/**: Directory containing example test files.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure your code follows the existing style and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

If you like this project, please give it a ⭐!
