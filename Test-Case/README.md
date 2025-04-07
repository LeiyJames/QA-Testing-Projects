# 🧪 Step-by-Step Guide for Testing LW Portals

Welcome to the **LW Portals** testing repository! This guide is meant to help you follow a smooth and efficient process for executing test cases across three key portals:

- **HP**: Home Portal
- **GP**: Guest Portal
- **BP**: Business Portal

---

## 🛠️ Step 1: Get Set Up

Before diving into the testing process, ensure that you have access to the following:

1. **GitHub Access**:
   - Clone this repository to your local machine if you haven’t already.

2. **Testing Files**:
   - Open the `LW Portals TC.xlsx` file located in this repo.
   - This Excel sheet contains test cases for each portal (HP, GP, and BP).

3. **Tools**:
   - Ensure you have any necessary tools (e.g., browser, login credentials) to execute the test cases on the portals.

---

## 📁 Step 2: Understand the Test Cases Layout

The test cases are categorized under three sheets in the Excel file:

1. **HP TC** (Home Portal)
   - Focus: `HP_Login Functionality`
2. **GP TC** (Guest Portal)
   - Focus: `GP_Login Functionality`
3. **BP TC** (Business Portal)
   - Focus: `BP_Login Functionality`

Each sheet contains the following columns:
- **Created By**: Name of the author (Leigh).
- **Date Created**: Date the test case was created.
- **Test Case**: Descriptions of the specific tests.
- **Execution Status**: Marks whether the test is Passed, Failed, or Needs Review.

---

## 💻 Step 3: Select a Portal to Test

1. Open the Excel file.
2. Choose the sheet corresponding to the portal you wish to test:
   - **HP TC** for Home Portal.
   - **GP TC** for Guest Portal.
   - **BP TC** for Business Portal.

---

## ✅ Step 4: Execute the Test Cases

1. **Read the Test Case**:
   - Carefully read the steps outlined for the test case.
   
2. **Perform the Test**:
   - Follow each step in the test case exactly as described.
   - Ensure you’re testing the portal in the environment where the login functionality needs validation.

3. **Mark the Test Status**:
   - After completing the test case, mark the execution status:
     - **Pass**: If the functionality works as expected.
     - **Fail**: If the functionality does not work as expected.
     - **Needs Review**: If further clarification or fixes are needed.

---

## 🧩 Step 5: Document Issues

If any issues are encountered during testing:

1. **Bug Reporting**:
   - Log a bug in your issue tracker (e.g., GitHub Issues, Jira).
   - Include detailed information like steps to reproduce, expected vs. actual behavior, and screenshots if possible.

2. **Link to Test Case**:
   - Reference the test case in the issue tracker to maintain context.

---

## 🔄 Step 6: Iterate and Retest

- Once bugs are fixed, revisit the test cases and **retest** any failed cases.
- Make sure to **update the execution status** in the Excel file to reflect the results of your retesting.
  
---

## 🔄 Step 7: Automation (Future-Ready)

- As the test cases become stable, consider migrating them to an automated testing framework (e.g., **Cypress** or **Playwright**).
- Use the steps documented in these test cases to create automated scripts that validate login functionalities across different portals.

---

## 📅 Step 8: Tracking and Reporting

- **Monitor Progress**:
  - Keep track of your test execution statuses to ensure everything is on track.
  
- **Reporting**:
  - After completing the tests, generate a summary report showing the test results and any critical issues found.

---

## 🙌 Credits

- **Creator**: Leigh (QA Tester)

---

