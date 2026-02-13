import os
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage(Page):
    EMAIL = os.getenv("TEST_EMAIL")
    PASSWORD = os.getenv("TEST_PASSWORD")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[wized="emailInput"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[wized="passwordInput"]')
    CONTINUE_BUTTON = (By.XPATH, '//a[@class="login-button w-button"]')
    ERROE_MSG =(By.XPATH, '//div[@class="error-message"]')


    def open_sign_in_page(self):
        self.open_url('https://soft.reelly.io/sign-in')
        self.wait_until_element_present(*self.EMAIL_FIELD)

    def log_in_to_page(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password,*self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BUTTON)
       # actual_text = self.driver.find_element(*self.ERROE_MSG).text
        #assert 'incorrect' in actual_text.lower(),\
         #   f'Login error message not show. Got: {actual_text}'




