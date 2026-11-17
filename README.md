# SauceDemo QA Automation Framework

Automated end-to-end UI test suite for [SauceDemo](https://www.saucedemo.com/) built with **Python**, **Selenium WebDriver**, and **PyTest** following the **Page Object Model (POM)** design pattern.

## Project Structure

- `login_page.py`: Page Object class encapsulating web elements and user actions for the Login page.
- `test_login.py`: PyTest suite covering positive and negative authentication scenarios.
- `requirements.txt`: Project dependencies.

## Test Scenarios Covered

1. **Successful Login (`test_login_exitoso`):** Verifies that a valid user (`standard_user`) is redirected to the inventory page.
2. **Invalid Login (`test_login_fallido`):** Verifies that invalid credentials trigger the expected authentication error message.

## Setup & Execution

1. Clone the repository and create a virtual environment:
   ```bash
   python -m venv .venv