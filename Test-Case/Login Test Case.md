# Login Test Cases

## Module: Login_Functionality
- **Test Case ID:** Login_TC01  
- **Tester Name:** Leigh James  
- **Test Description:** Valid & invalid logins, empty fields, and error messages.  

### Functional Test Cases

| Test Case ID | Test Case Description       | Test Data          | Steps                                                                 | Expected Result                                  | Actual Result | Status |
|--------------|----------------------------|--------------------|-----------------------------------------------------------------------|--------------------------------------------------|---------------|--------|
| TC001        | Valid Login                | Testuser / Test@123 | 1. Enter valid username.<br>2. Enter valid password.<br>3. Click "Login." | User logs in successfully. Redirect to dashboard/homepage. |               | Pass   |
| TC002        | Invalid Username           | estuser / Test@123  | 1. Enter invalid username.<br>2. Enter valid password.<br>3. Click "Login." | Error: "Invalid username or password."           |               | Pass   |
| TC003        | Invalid Password           | Testuser / Test123  | 1. Enter valid username.<br>2. Enter invalid password.<br>3. Click "Login." | Error: "Invalid username or password."           |               | Pass   |
| TC004        | Empty Username             |                    | 1. Leave username blank.<br>2. Enter password.<br>3. Click "Login."  | Error: "Username is required."                   |               |        |
| TC005        | Empty Password             |                    | 1. Enter username.<br>2. Leave password blank.<br>3. Click "Login."  | Error: "Password is required."                   |               |        |
| TC006        | Empty Both Fields          |                    | 1. Leave both fields blank.<br>2. Click "Login."                     | Errors: "Username & Password are required."      |               |        |

---

## Module: Login_ UI & Usability
- **Test Case ID:** Login_TC01  
- **Tester Name:** Leigh James  
- **Test Description:** Valid & invalid logins, empty fields, and error messages.  

### UI & Usability Test Cases

| Test Case ID | Test Case Description       | Steps                                                                 | Expected Result                                  | Actual Result | Status |
|--------------|----------------------------|-----------------------------------------------------------------------|--------------------------------------------------|---------------|--------|
| TC001        | Placeholder Text           | 1. Check username/password fields.                                   | Placeholders: "Enter username" & "Enter password." |               | Pass   |
| TC002        | Password Masking           | 1. Type in password field.                                           | Password is hidden (****).                       |               | Pass   |
| TC003        | Responsive Design          | 1. Test on mobile/tablet.<br>2. Resize browser.                      | Login form adjusts correctly.                    |               | Pass   |

---

## Module: Login_ Security
- **Test Case ID:** Login_TC01  
- **Tester Name:** Leigh James  
- **Test Description:** Tests SQL injection, XSS, and brute-force protection.  

### Basic Security Test Cases

| Test Case ID | Test Case Description       | Steps                                                                 | Expected Result                                  | Actual Result | Status |
|--------------|----------------------------|-----------------------------------------------------------------------|--------------------------------------------------|---------------|--------|
| TC001        | SQL Injection              | 1. Enter ' OR '1'='1 in username.<br>2. Click "Login."               | Error: "Invalid credentials." No DB breach.      |               | Pass   |
| TC002        | XSS Attempt                | 1. Enter <script>alert('XSS')</script> in fields.<br>2. Click "Login." | Script is sanitized/blocked.                     |               | Pass   |
| TC003        | Brute Force Protection     | 1. Fail login 5+ times.                                              | Account locked temporarily. Captcha appears.     |               | Pass   |

---

## Module: Login_Forgot Password/Email
- **Test Case ID:** Login_TC01  
- **Tester Name:** Leigh James  
- **Test Description:** Covers reset link, valid/invalid email submission, and password update.  

### Forgot Password/Email Test Cases

| Test Case ID | Test Case Description       | Steps                                                                 | Expected Result                                  | Actual Result | Status |
|--------------|----------------------------|-----------------------------------------------------------------------|--------------------------------------------------|---------------|--------|
| TC001        | Forgot Password Link       | 1. Click "Forgot Password."                                          | Error: "Invalid credentials." No DB breach.      |               | Pass   |
| TC002        | Valid Email Submission     | 1. Enter registered email.<br>2. Click "Submit."                     | Confirmation: "Reset link sent to email."        |               |        |
| TC003        | Invalid Email Submission   | 1. Enter unregistered email.<br>2. Click "Submit."                   | Error: "Email not found."                        |               | Pass   |
| TC004        | Empty Email Field          | 1. Leave email blank.<br>2. Click "Submit."                          | Error: "Email is required."                      |               | Pass   |
| TC005        | Reset Password Flow        | 1. Open reset link from email.<br>2. Enter new password.<br>3. Confirm new password.<br>4. Submit. | Success: "Password updated. Please login." |               |        |