\# ✅ Manual Test Cases - Login Functionality

This document contains test cases for the \*\*Login\*\* functionality of
the application.

\## 🔍 Test Summary

\| Test Case ID \| Title \| Description \| Precondition \| Steps to
Reproduce \| Expected Result \| Status \|
\|\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\--\|
\| TC001 \| Login with valid user \| Ensure users can log in with
correct credentials \| User is registered \| 1. Go to login page\<br\>2.
Enter valid email\<br\>3. Enter valid password\<br\>4. Click Login \|
User is redirected to the dashboard \| Pass \| \| TC002 \| Login with
invalid password \| Ensure error message appears for incorrect password
\| User is registered \| 1. Go to login page\<br\>2. Enter valid
email\<br\>3. Enter wrong password\<br\>4. Click Login \| Error message:
\"Invalid credentials\" \| Pass \| \| TC003 \| Login with blank fields
\| Check validation messages when fields are empty \| N/A \| 1. Go to
login page\<br\>2. Leave email and password blank\<br\>3. Click Login \|
Validation messages: \"Email required\", etc. \| Pass \| \| TC004 \|
Remember Me checkbox \| Ensure \'Remember Me\' retains login \| User is
registered \| 1. Check \'Remember Me\'\<br\>2. Login\<br\>3. Close and
reopen browser \| User is still logged in \| Pass \|

\## 🛠 Environment - Browser: Chrome v123 - OS: Windows 10 - URL:
https://example.com/login

\## 👤 Author \[Your Name\](https://www.linkedin.com/in/your-profile)
