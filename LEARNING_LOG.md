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

## Day 10 – Page Object Model (POM) Introduction
- Created `pages/` folder and implemented first Page Object (`DropdownPage`)
- Moved locators and page actions from test into Page Object class
- Updated tests to interact through Page Object methods instead of direct locators
- Faced real timeout failure due to slow mobile network and fixed by increasing navigation timeout
- Successfully executed multiple tests using POM structure

**Key Learning:**  
Page Object Model separates test logic from UI implementation, making automation scalable, maintainable, and closer to real industry frameworks.

---
