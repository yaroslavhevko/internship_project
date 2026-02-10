from behave.pathutil import PATH_LIKE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from sample_script import driver_path

driver_path = ChromeDriverManager().install()
#Start Chrome browser:
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# Open amazon.com
driver.get("https://amazon.com/")

#locators

#For Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#For sign in line

#By ID
driver.find_element(By.ID,'claim-input-container')
driver.find_element(By.ID, 'ap_email_login')

#By XPATH
driver.find_element(By.XPATH, '//input[@type="email"]')
driver.find_element(By.XPATH, '//div[@class="a-section a-spacing-micro"]')

#For Continue button

#By ID
driver.find_element(By.ID, 'continue')
driver.find_element(By.ID, 'continue-announce')

#By XPATH
driver.find_element(By.XPATH, '//input[@class="a-button-input"]')
driver.find_element(By.XPATH,'//span[@class="a-button-text a-text-center"]')

#For  Conditions of Use
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

#For Privacy Notice
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")

#For Need Help?
driver.find_element(By.XPATH,"//a[text()='Need Hepl?']")
driver.find_element(By.XPATH,"//span[class='a-list-item']")

#For Create a free business account
driver.find_element(By.ID,'ab-registration-ingress-link')
driver.find_element(By.XPATH,"//span[text()='Create a free business account']")


driver.quit()
