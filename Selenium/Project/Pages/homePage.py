from selenium.webdriver.common.by import By
from Selenium.Project.Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.userdropdown_classname = Locators.userdropdown_classname
        self.logout_button_linktext = Locators.logout_button_linktext

    def is_userdropdown_present(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.userdropdown_classname)))
            return True
        except:
            return False

    def click_userdropdown(self):
        userdropdown = self.driver.find_element(By.CLASS_NAME, self.userdropdown_classname)
        userdropdown.click()

    def click_logout(self):
        logout_button = self.driver.find_element(By.LINK_TEXT, self.logout_button_linktext)
        logout_button.click()