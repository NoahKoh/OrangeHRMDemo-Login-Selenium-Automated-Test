from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/chromedriver") #Driver path
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)
driver.maximize_window()

email_field = driver.find_element(By.NAME, "username")
email_field.send_keys("Admin")
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")
login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
login_button.click()

driver.implicitly_wait(30)

driver.quit()


