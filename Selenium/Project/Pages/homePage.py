from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.userdropdown_classname = "oxd-userdropdown-tab"
        self.logout_button_linktext = "Logout"

    def click_userdropdown(self):
        userdropdown = self.driver.find_element(By.CLASS_NAME, self.userdropdown_classname)
        userdropdown.click()

    def click_logout(self):
        logout_button = self.driver.find_element(By.LINK_TEXT, self.logout_button_linktext)
        logout_button.click()