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
driver.get("https://www.target.com/")

#For Account
driver.find_element(By.ID,'account-sign-in')
driver.find_element(By.XPATH,"//*[@data-test='@web/AccountLink']").click()

#Verification
expected ='Sign in or create account'
actual = driver.find_element(By.XPATH,"//h1[contains(@class, 'styles_ndsHeading')]").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'

# For Verification
driver.find_element(By.XPATH,"//*[@data-test='accountNav-signIn']").click()
driver.find_element(By.XPATH,"//button[text()='Sign in or create account']")

driver.find_element(By.ID, 'login')

driver.quit()