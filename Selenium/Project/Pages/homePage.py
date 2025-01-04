from selenium.webdriver.common.by import By
from Selenium.Project.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.userdropdown_classname = Locators.userdropdown_classname
        self.logout_button_linktext = Locators.logout_button_linktext

    def click_userdropdown(self):
        userdropdown = self.driver.find_element(By.CLASS_NAME, self.userdropdown_classname)
        userdropdown.click()

    def click_logout(self):
        logout_button = self.driver.find_element(By.LINK_TEXT, self.logout_button_linktext)
        logout_button.click()