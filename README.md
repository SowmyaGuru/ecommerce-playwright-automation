# E-Commerce Playwright Automation Framework

## Project Overview
This repository contains a UI automation framework developed using Python, Playwright and PyTest to automate critical e-commerce application workflows.

The framework follows the Page Object Model (POM) design pattern and is designed to be scalable, reusable and maintainable.

## Application Under Test
- Application: SauceDemo
- URL: https://www.saucedemo.com/
- Testing Type: UI Automation

## Technology Stack
- Python
- Playwright
- PyTest
- Page Object Model (POM)
- Git and GitHub
- Allure Reporting
- GitHub Actions

## Test Coverage
- Login and authentication
- Product listing and sorting
- Shopping cart
- Checkout workflow
- Negative and boundary scenarios

## Framework Architecture
- tests/: Contains automated test cases.
- pages/: Contains page objects, locators and UI actions.
- test_data/: Contains external test data.
- utils/: Contains reusable utilities.
- conftest.py: Shared PyTest fixtures.
- pytest.ini: PyTest configuration.
- requirements.txt: Project dependencies.

## Setup Instructions

### 1. Clone the repository
```bash
git clone &lt;repository-url&gt;
```

### 2. Navigate to the project
```bash
cd ecommerce-playwright-automation
```

### 3. Create a virtual environment
```bash
python -m venv venv
```

### 4. Activate the environment (Windows)
```bash
venv\Scripts\activate
```

### 5. Install dependencies
```bash
pip install -r requirements.txt
```

### 6. Install Playwright browsers
```bash
playwright install
```

## Test Execution

Run all tests:
```bash
pytest -v
```

Run a specific test:
```bash
pytest tests/test_login.py -v
```

## Contribution Guidelines
- Create a feature branch for every change.
- Follow the Page Object Model.
- Use meaningful test and method names.
- Avoid hardcoded credentials.
- Run tests locally before raising a Pull Request.
- Ensure code is reviewed before merging into the main branch.

## Reporting
Allure reporting will be integrated as part of the framework implementation.

## Project Status
Framework initialization and UI automation development are in progress.
