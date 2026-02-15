# Learning Log – Playwright Python Automation

This file tracks my **day-by-day hands-on progress**
while learning **QA Automation using Playwright, Python, and PyTest**.

---

## Day 1 – Setup & First Run
- Installed Python and Playwright
- Successfully launched browser using Playwright
- Verified environment setup

---

## Day 2 – Locators & Basic Actions
- Learned element locators
- Performed fill, click, and navigation actions
- Understood interaction flow in automation

---

## Day 3 – Conditions vs Assertions
- Difference between `if` logic and `assert` verification
- Handling buttons and checkboxes
- Real meaning of test validation

---

## Day 4 – Dropdowns & Wait Strategies
- Selected dropdown options
- Learned smart waits vs hard waits
- Prevented flaky test behavior

---

## Day 5 – Real Assertion Behavior
- Observed pass vs fail execution
- Understood browser closing on failure
- Learned importance of true verification

---

## Day 6 – Project Structure & Python Modules
- Separated `tests`, `utils`, and `practice`
- Learned Python package concept
- Executed modules using `python -m`

---

## Day 7 – PyTest Framework Introduction
- Installed and configured PyTest
- Learned automatic test discovery
- Controlled execution using `pytest.ini`

---

## Day 8 – PyTest Fixtures
- Implemented browser fixture in `conftest.py`
- Automatic setup and teardown
- Clean and scalable test design

---

## Day 9 – Multiple Tests with Shared Fixture
- Added second test case to verify page title
- Executed multiple tests using the same PyTest fixture
- Observed automatic browser setup and teardown for each test
- Understood scalability of test framework without duplicate code

**Key Learning:**  
One fixture can support multiple tests, enabling scalable and maintainable automation.

---

## Day 10 – Page Object Model (POM) Introduction
- Created `pages/` folder and implemented first Page Object (`DropdownPage`)
- Moved locators and page actions from test into Page Object class
- Updated tests to interact through Page Object methods instead of direct locators
- Faced real timeout failure due to slow mobile network and fixed by increasing navigation timeout
- Successfully executed multiple tests using POM structure

**Key Learning:**  
Page Object Model separates test logic from UI implementation, making automation scalable, maintainable, and closer to real industry frameworks.

---

## Day 11 – Reusable Verification in Page Object
- Added reusable verification method `is_option_selected()` inside Page Object
- Reduced duplication of assertion logic in test cases
- Improved readability of tests using business-level assertions
- Successfully executed tests after Page Object enhancement

**Key Learning:**  
Reusable verification helpers inside Page Objects improve readability, scalability, and maintainability of automation frameworks.

---

## Day 12 – Multiple Page Objects
- Created second Page Object for Checkboxes page
- Implemented reusable actions and verification in new page class
- Added separate test file for checkbox behavior
- Executed multiple Page Objects within single PyTest framework

**Key Learning:**  
Automation frameworks handle multiple independent pages using separate Page Objects while still running under one shared structure and execution.

---

## Day 13 – Navigation Between Page Objects
- Implemented navigation from Checkboxes page to Dropdown page
- Returned next Page Object after navigation to model real user flow
- Added navigation flow test case
- Learned to verify navigation using page-specific elements instead of titles

**Key Learning:**  
Real automation frameworks connect Page Objects through navigation and validate pages using unique UI elements for reliable testing.

---

## Day 14 – Test Data Parameterization
- Converted dropdown test to parameterized execution using PyTest
- Executed same test logic with multiple data inputs
- Learned separation of test logic and test data
- Understood importance of external data sources in real frameworks

**Key Learning:**  
Data-driven testing improves scalability, reusability, and maintainability by separating test logic from test data.

---

## Day 15 – Behavioral Assertions
- Enhanced checkbox test to verify state before and after user action
- Implemented Arrange → Act → Assert testing pattern
- Learned importance of preventing false positives in automation

**Key Learning:**  
Good tests must validate behavior change caused by user action, not just final static state.

---

## Day 16 – Base Test Architecture
- Introduced BaseTest layer for shared test behavior
- Converted checkbox test to class-based structure
- Learned importance of centralized setup and scalability in frameworks

**Key Learning:**  
Real automation frameworks use a Base Test layer to centralize shared logic, keeping tests clean, reusable, and scalable.

---


