from selenium.webdriver.common.by import By
from Selenium.Project.Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
        self.error_message_classname = Locators.error_message_classname

    def enter_username(self, username):
        username_field = self.driver.find_element(By.NAME, self.username_textbox_name)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, self.password_textbox_name)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, self.login_button_xpath)
        login_button.click()

    def get_error_message(self):
        error_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.error_message_classname)))
        return error_message.text