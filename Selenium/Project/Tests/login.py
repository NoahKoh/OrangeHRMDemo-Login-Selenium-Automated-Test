import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Selenium.Project.Pages.loginPage import LoginPage
from Selenium.Project.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service("/chromedriver") # Driver path
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        self.assertTrue(homepage.is_userdropdown_present(), "Login fail. User dropdown not found")
        homepage.click_userdropdown()
        homepage.click_logout()

        time.sleep(2)

    def test_02_login_invalid_email(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("InvalidUser")
        login.enter_password("admin123")
        login.click_login()
        error_message = login.get_error_message()
        self.assertEqual(error_message, "Invalid credentials", "Error message text does not match")

    def test_03_login_invalid_password(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("InvalidPassword")
        login.click_login()
        error_message = login.get_error_message()
        self.assertEqual(error_message, "Invalid credentials", "Error message text does not match")

    def test_04_login_invalid_email_password(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("InvalidUser")
        login.enter_password("InvalidPassword")
        login.click_login()
        error_message = login.get_error_message()
        self.assertEqual(error_message, "Invalid credentials", "Error message text does not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Selenium/Reports")) # Report Directory Path