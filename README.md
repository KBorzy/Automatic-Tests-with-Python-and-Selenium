# Automation tests with Python and Selenium

## Folder Structure:
### 1. actions:
#### This folder contains the Actions.py file, which includes functions for common actions performed on web elements, such as click(element), sendKeys(inputField, value), and getText(element). These functions can be reused across different test cases to interact with web elements.

2. pages:
This folder contains separate Python files for each page of the website being tested. For example, LoginPage.py and UserPage.py would be included in this folder. These files contain functions that define the actions that can be performed on each respective page, such as logging in, navigating to different pages, or interacting with elements on the page.

3. resources:
This folder contains resources that are required for the tests, such as the chromedriver.exe executable file for running Selenium tests with Chrome browser, and the input_data.xlsx file that contains test data for logging in, with email and password information stored in the first row and second column of the sheet.

4. utilities:
This folder contains utility functions that are used across the test project. For example, the Data.py file might include a function like getTestInputData() which reads the input_data.xlsx file and returns a dictionary with the email and password data needed for logging in.

5. tests:
This folder contains test cases that are implemented using pytest framework. The conftest.py file in this folder includes the configuration and setup for the tests. The login_test.py file would be an example of a test case for logging in, where pytest would execute the test and report the results.

Usage:
Clone the repository to your local machine.
Install the required dependencies, such as pytest and Selenium.
Update the input_data.xlsx file in the resources folder with the appropriate email and password data for testing.
Implement test cases in the tests folder using pytest framework, importing the necessary actions and pages from the actions and pages folders respectively.
Run the tests using pytest, and review the test results.
That's it! You're now ready to write and run tests for the web application using pytest and Selenium. Happy testing!
