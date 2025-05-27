# Captive Portal Test Cases

## Module: Captive Portal Popup Test Case
- **Tester Name:** Leigh James  
- **Description:** Verify if the captive portal pop-up appears in different scenarios.  
- **Prerequisites:**  
  1. Stable WiFi connection  
  2. Browser (Chrome, Firefox, Edge, etc.)  
- **Environment:**  
  1. Device: Android/iOS  

### Popup Test Cases

| Test Case ID | Test Device               | Test Steps                                                                 | Expected Result                                  | Status |
|--------------|---------------------------|----------------------------------------------------------------------------|--------------------------------------------------|--------|
| TC001        | iOS (iPhone15)            | 1. Turn on WiFi                                                            | Captive portal should pop up automatically       | Pass   |
|              | iOS (iPhone12)            | 2. Tap Captive Portal WiFi                                                 | Captive portal should pop up automatically       | Pass   |
|              | Android (Xiaomi11)        |                                                                            | Captive portal should pop up automatically       | Pass   |
|              | Old Android (Galaxy A01)  |                                                                            | Captive portal should pop up automatically       | Pass   |
|              | Android (Redmi A3)        |                                                                            | Captive portal should pop up automatically       | Pass   |
|              | Web                       |                                                                            | Captive portal should pop up automatically       | Pass   |
| TC002        | iOS (iPhone15)            | 1. Turn on WiFi                                                            | Captive portal should pop up automatically       | Fail   |
|              | iOS (iPhone12)            | 2. Tap Captive Portal WiFi                                                 | Captive portal should pop up automatically       | Fail   |
|              | Android (Xiaomi11)        | Tap cancel "Use Without Internet" (iOS only)                               | Captive portal should pop up automatically       | Pass   |
|              | Old Android (Galaxy A01)  | Tap three dot "Use this network as is" (Android)                          | Captive portal should pop up automatically       | Pass   |
|              | Android (Redmi A3)        | 3. Turn off WiFi                                                           | Captive portal should pop up automatically       | Pass   |
|              | Web                       | 4. Wait for 2 minutes                                                      | Captive portal should pop up automatically       | Pass   |
| TC003        | iOS (iPhone15)            | 1. Turn on WiFi<br>2. Tap Captive Portal WiFi<br>3. Enter voucher (Q6KU6F) | Captive portal should pop up automatically       | Pass   |
|              | Android (Xiaomi11)        | 4. Check internet (open YT)<br>5. Connect to other WiFi                    | Captive portal should pop up automatically       | Pass   |
|              | Web                       | 6. Wait for 2 mins<br>7. Reconnect to Captive Portal WiFi                 | Captive portal should pop up automatically       | Pass   |
| TC004        | iOS (iPhone15)            | 1. Turn on WiFi<br>2. Tap Captive Portal WiFi                              | Captive portal should pop up automatically       | Fail   |
|              | Android (Xiaomi11)        | 3. Enter voucher (Q6KU6F)<br>4. Forget network                             | Captive portal should pop up automatically       | Fail   |
|              | Web                       | 5. Restart WiFi<br>6. Reconnect                                           | Captive portal should pop up automatically       | Fail   |
| TC005        | iOS (iPhone15)            | 1. Turn on WiFi<br>2. Tap Captive Portal WiFi                              | Captive portal should pop up automatically       | Pass   |
|              | Android (Xiaomi11)        | Tap cancel "Use Without Internet"<br>3. Forget network                    | Captive portal should pop up automatically       | Pass   |
|              | Web                       | 4. Restart WiFi<br>5. Reconnect                                           | Captive portal should pop up automatically       | Pass   |
| TC006        | iOS (iPhone15)            | 1. Turn on WiFi<br>2. Tap Captive Portal WiFi                              | Captive portal should pop up automatically       | Pass   |
|              | Android (Xiaomi11)        | 3. Connect to another WiFi network<br>4. Wait 2 mins                      | Captive portal should pop up automatically       | Pass   |
| TC007        | iOS (iPhone15)            | 1. Turn on WiFi<br>2. Tap Captive Portal WiFi                              | Captive portal should pop up automatically       | Pass   |
|              | Android (Xiaomi11)        | 3. Enter voucher (Q6KU6F)<br>4. Connect to other WiFi                     | Captive portal should pop up automatically       | Pass   |
| TC008        | iOS (iPhone15)            | 1. Turn on WiFi<br>2. Tap Captive Portal WiFi                              | Captive portal should pop up automatically       | Fail   |
|              | Android (Xiaomi11)        | Tap cancel "Use Without Internet"<br>4. Connect to other WiFi             | Captive portal should pop up automatically       | Pass   |
| TC009        | iOS (iPhone15)            | 1. Turn on WiFi<br>2. Tap Captive Portal WiFi                              | Captive portal should pop up automatically       | Pass   |
|              | Android (Xiaomi11)        | 3. Wait until phone screen lock<br>4. Unlock phone                        | Captive portal should pop up automatically       | Pass   |

---

## Module: Captive Portal Flow
- **Tester Name:** Leigh James  
- **Description:** Verify overall functionality from login until successful voucher payment.  
- **Prerequisites:**  
  1. Stable WiFi connection  
  2. Browser (Chrome, Firefox, Edge, etc.)  
- **Environment:**  
  1. Device: Android/iOS  

### Portal Flow Test Cases

| Test Case ID | Test Description                                      | Precondition               | Test Data                     | Status |
|--------------|-------------------------------------------------------|----------------------------|-------------------------------|--------|
| TC001        | Test if user can connect with an empty field          |                            |                               | Pass   |
| TC002        | Test if user can connect after input valid voucher    | Valid voucher code         | Voucher code: Q6KU6F          | Pass   |
| TC003        | Test if user can connect after input invalid voucher  | Invalid voucher code       | Voucher code: Q6KU78          | Pass   |
| TC004        | Test if empty Captive portal account ID can buy voucher |                            |                               | Pass   |
| TC005        | Test if valid Captive portal account ID can proceed   |                            | Captive Portal ID: 35456457   | Pass   |
| TC006        | Test if invalid Captive portal account ID can't proceed |                            | Captive Portal ID: 101010101  | Pass   |
| TC007        | Verify unpaid voucher within a minute fails transaction | Selected payment method<br>Account has load balance | | Pass   |