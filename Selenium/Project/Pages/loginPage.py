from selenium.webdriver.common.by import By
from Selenium.Project.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath

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