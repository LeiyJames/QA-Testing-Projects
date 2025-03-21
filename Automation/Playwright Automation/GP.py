from playwright.sync_api import sync_playwright

def test_website(browser_name, iterations=1):
    with sync_playwright() as p:
        for i in range(iterations):
            print(f"Running test iteration {i+1} on {browser_name}...")

            # Select the browser
            if browser_name == "chrome":
                browser = p.chromium.launch(headless=False, slow_mo=500, channel="chrome")
            elif browser_name == "firefox":
                browser = p.firefox.launch(headless=False, slow_mo=500)
            else:
                raise ValueError("Unsupported browser! Choose 'chrome' or 'firefox'.")

            context = browser.new_context()
            page = context.new_page()

            try:
                page.goto("URL COMPANY PROJECT", timeout=60000)

                # Login
                page.fill("input[type='text']", "USERNAME")
                page.fill("input[type='password']", "PASSWORD")
                page.click(".login-btn")

                page.wait_for_load_state("networkidle", timeout=50000)

                print(f"✅ Login successful on {browser_name}. Simulating session timeout...")

                page.wait_for_selector(".page-controller", timeout=50000)

                # Scroll down
                for _ in range(3): 
                    page.evaluate("window.scrollBy(0, 300)")
                    page.wait_for_timeout(1000)

                # Settings
                page.hover(".profile-container")
                page.wait_for_selector(".dropdown-content", state="visible", timeout=50000)
                page.click("text=Settings")

                # Navigate to Profile
                page.hover(".profile-container")
                page.wait_for_selector(".dropdown-content", state="visible", timeout=50000)
                page.click("text=Profile")

                # Scroll down
                for _ in range(3): 
                    page.evaluate("window.scrollBy(0, 300)")
                    page.wait_for_timeout(1000)

                # Change password
                page.hover(".profile-container")
                page.wait_for_selector(".dropdown-content", state="visible", timeout=50000)
                page.click("text=Change Password")

                #Password Form
                password_fields = page.locator("input.input-style")
                password_fields.nth(0).fill("goods") 
                password_fields.nth(0).fill("") 
                password_fields.nth(0).fill("P@ssw0rd123") 

                password_fields.nth(1).fill("P@ssw0rd123") 
                password_fields.nth(1).fill("")  
                password_fields.nth(1).fill("Apps1234577")  

                password_fields.nth(2).fill("P@ssw0rd123")  
                password_fields.nth(2).fill("")
                password_fields.nth(2).fill("1234577")

                # Logout
                page.hover(".profile-container")
                page.wait_for_selector(".dropdown-content", state="visible", timeout=50000)
                page.locator("text=Logout").nth(0).click()

                page.wait_for_timeout(3000)

                print(f"✅ Test iteration {i+1} on {browser_name} completed successfully.\n")

            except Exception as e:
                error_screenshot = f"error_screenshot_{browser_name}_{i+1}.png"
                page.screenshot(path=error_screenshot)
                print(f"⚠️ Error in test iteration {i+1} on {browser_name}: {e}")
                print(f"🖼 Screenshot saved: {error_screenshot}")

            finally:
                # Clear session data and ensure a new session
                context.clear_cookies()
                page.evaluate("window.localStorage.clear();")
                page.evaluate("window.sessionStorage.clear();")

                # Close the context before creating a new one
                context.close()

                # Open a new browser context to simulate a new session
                context = browser.new_context()
                page = context.new_page()
                page.goto("URL COMPANY PROJECT")

                # Verify if redirected to login page
                if "login" in page.url:
                    print(f"✅ Session timeout simulated successfully on {browser_name}!")
                else:
                    print(f"❌ Session did not expire as expected on {browser_name}.")

                browser.close()

# Run the test in both Chrome and Firefox
for browser in ["chrome", "firefox"]:
    test_website(browser, iterations=1)
