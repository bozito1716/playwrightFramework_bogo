# Playwright Automation Framework

A scalable end-to-end test automation framework built with **Playwright**, **Python**, and **Pytest**, following the **Page Object Model (POM)** design pattern.

This framework is designed with maintainability, scalability, and reusability in mind, making it easy to expand as applications grow.

> **Note:** This repository showcases the automation framework only. The application under test is private and is not included in this repository.

---

## Features

- Page Object Model (POM) architecture
- Reusable `BasePage` for shared actions and assertions
- Centralized configuration using environment variables
- Pytest fixtures for browser and page lifecycle management
- Stable locator strategy using `data-testid`
- HTML test reporting
- Organized project structure for long-term maintainability
- Easy to extend with new pages and test suites

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| Playwright | Browser Automation |
| Pytest | Test Runner |
| pytest-html | HTML Reports |
| python-dotenv | Environment Configuration |

---

## Project Structure

```text
playwright-automation-framework/
│   ai/
│   └── failure_analyzer.py
│   └── prompts.py
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── home_page.py
│   └── how_it_works_page.py
|   └── sign_up_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_home_page.py
│
├── utils/
│   └── test_data.py
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd playwright-automation-framework
```

### Create a virtual environment

```bash
python -m venv .venv
```

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
BASE_URL=<application_url>
LOGIN_URL=<login_url>

VALID_EMAIL=<test_email>
VALID_PASSWORD=<test_password>
```

---

## Running Tests

Run the entire suite

```bash
pytest
```

Run a specific test file

```bash
pytest tests/test_login.py
```

Run a single test

```bash
pytest tests/test_login.py::test_successful_login
```

HTML reports are automatically generated after each execution.

---

## Framework Architecture

The framework follows the **Page Object Model (POM)** to separate UI interactions from test logic.

### BasePage

The `BasePage` contains reusable browser interactions, waits, assertions, and helper methods shared across all page objects.

### Page Objects

Each page object encapsulates:

- Locators
- User interactions
- Page-specific validations

This approach improves readability, reduces code duplication, and simplifies maintenance.

---

## Current Coverage

The framework currently includes automated tests for:

- Authentication workflows
- Form validation
- Positive and negative scenarios
- Navigation verification
- UI element visibility
- Button state validation

The architecture is designed to support additional pages and features with minimal changes.

---

## Reporting

Test execution generates self-contained HTML reports that include:

- Execution summary
- Passed and failed tests
- Execution time
- Detailed failure information

---

## Design Principles

This framework was built around software engineering best practices:

- Separation of concerns
- Reusable components
- Maintainable architecture
- Scalable project structure
- Stable locator strategy
- Readable test cases
- Environment-based configuration

---

## Roadmap

Planned enhancements include:

- GitHub Actions CI/CD
- Cross-browser execution
- Parallel test execution
- Screenshot capture on failures
- Video and trace collection
- API testing integration
- AI-assisted test failure analysis
- Visual regression testing

---

## License

This project is provided for educational and portfolio purposes.