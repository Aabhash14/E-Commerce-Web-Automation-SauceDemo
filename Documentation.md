TEST PLAN
‘E-Commerce Web Automation – SauceDemo’

1. Document Information
•	Project Name: E-commerce Website Automation
•	Application Under Test (AUT): SauceDemo
•	URL: https://www.saucedemo.com
•	Test Type: Functional Testing + Performance Validation
•	Automation Tool: Selenium WebDriver
•	Programming Language: Python
•	Test Framework: Pytest
•	Design Pattern: Page Object Model (POM)
•	Reporting Tool: Allure
•	Browser: Google Chrome
•	OS: Windows
 
2. Objective
The objective of this test plan is to validate the end-to-end functionality and performance of an e-commerce application by automating the complete user journey.
The scope includes:
•	Login validation
•	Product selection
•	Cart badge validation
•	Cart operations (add/remove)
•	Checkout and shipping process
•	Order completion
•	Logout
•	Performance measurement of critical actions
 
3. Scope of Testing
In-Scope
•	User login with valid credentials
•	Product selection from inventory
•	Cart badge count verification
•	Cart page validation
•	Product removal from cart
•	Checkout process
•	Shipping details entry
•	Order completion
•	Logout
•	Performance timing for key actions

Out of Scope
•	Payment gateway validation
•	Backend database validation
•	Security testing
•	Cross-browser testing
 
4. Test Environment
Component	Details
Browser	Chrome
Automation Tool	Selenium WebDriver
Language	Python
Framework	Pytest
Reporting	Allure
OS	Windows

 
5. Test Data
Valid User Credentials
Username	Password
standard_user	secret_sauce
problem_user	secret_sauce
performance_glitch_user	secret_sauce
error_user	secret_sauce
visual_user	secret_sauce
locked_out_user	secret_sauce

Product Used
•	Sauce Labs Backpack
•	Sauce Labs Bike Light

Shipping Details
Field	Value
First Name	Aabhash
Last Name	Shahi
Postal Code	44600

 
6. Test Strategy
•	Page Object Model (POM) is used for maintainability and reusability.
•	Pytest is used for test execution and assertions.
•	Allure is used for structured reporting.
•	Utility functions are used to measure performance metrics.
•	Functional and performance validations are combined in a single workflow.
•	Console logs are added for transparency of validation results.
 
7. Entry and Exit Criteria
Entry Criteria
•	Application is accessible
•	Test environment is stable
•	Browser and drivers are configured
Exit Criteria
•	All test steps executed successfully
•	Cart badge and cart item validations passed
•	Checkout flow completed successfully
•	Performance metrics recorded
•	No critical defects open
 
8. Detailed Test Scenario and Steps
Test Case ID: TC_ECOM_001
Test Case Title: Full E-commerce Flow with Cart Badge and Performance validation
Step-by-Step Execution
Step 1: Launch Application
•	Open browser
•	Navigate to SauceDemo homepage
•	Measure page load time
Expected Result:
•	Homepage loads successfully
•	Page load time is logged in console

Step 2: User Login
•	Enter valid username and password
•	Click Login
•	Measure login action time
Expected Result:
•	User is redirected to inventory page
•	Login time is recorded

Step 3: Add Products to Cart
•	Select multiple products from inventory
•	Click “Add to Cart” for each product
•	Measure time taken for each add-to-cart action
Expected Result:
•	Selected products are added successfully
•	Action time is logged

Step 4: Cart Badge Verification (Before Removal)
•	Count number of selected products
•	Read cart badge number
•	Compare both values
Expected Result:
•	Cart badge count equals number of products selected
•	Console prints
 
Step 5: Navigate to Cart
•	Click cart icon
•	Retrieve product list from cart
Expected Result:
•	Cart page opens
•	All selected products are visible
Step 6: Remove Products from Cart
•	Remove one product from cart
•	Measure removal action time
Expected Result:
•	Selected product is removed
•	Remaining products are displayed
Step 7: Cart Badge Verification (After Removal)
•	Count remaining cart items
•	Read updated cart badge value
•	Compare both values
Expected Result:
•	Cart badge count matches remaining items
•	Console prints:
 

Step 8: Checkout Process
•	Click Checkout
•	Enter shipping details
•	Continue checkout
Expected Result:
•	User proceeds to checkout overview page
•	Action execution time is logged

Step 9: Finish Order
•	Click Finish button
•	Measure completion time
Expected Result:
•	Order is completed successfully
•	User navigates to order confirmation page
Step 10: Logout
•	Logout from the application
•	Measure logout time
Expected Result:
•	User is logged out successfully
•	Redirected to login page

***For Detailed Manual Test Cases of SauceDemo***
link: https://docs.google.com/spreadsheets/d/1dmUTHfvBbkfOQSQ2Qf623zkN4BDThq8CLCZ1ioNGIkA/edit?usp=sharing

 
9. Performance Testing Approach
Performance is measured for:
•	Page load
•	Login action
•	Add to cart actions
•	Remove product action
•	Checkout actions
•	Logout

Metrics Captured:
•	Execution time (seconds)
•	Console output for each step
 
10. Reporting
•	Allure Report includes:
1.	Test steps
2.	Pass/Fail status
3.	Execution timeline

•	Console Logs include:
1.	Cart badge counts
2.	Selected product counts
3.	Performance metrics
 
11. Risks and Assumptions
Risks
•	Network latency may affect performance timing
•	UI changes may break locators

Assumptions
•	Test environment remains stable
•	Valid credentials are always available
 
12. Conclusion
This test plan validates both functional correctness and performance efficiency of an e-commerce web application. The automation ensures:
•	Accurate cart badge behavior
•	Reliable checkout flow
•	Measureable performance metrics
•	Maintainable and scalable test structure
