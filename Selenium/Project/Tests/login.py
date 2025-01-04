from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service("/chromedriver")  # Driver path
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        email_field = self.driver.find_element(By.NAME, "username")
        email_field.send_keys("Admin")
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("admin123")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_button.click()
        self.driver.implicitly_wait(10)
        userdropdown = self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
        userdropdown.click()
        logout_button = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete. Login Valid.")



if __name__ == '__main__':
    unittest.main()