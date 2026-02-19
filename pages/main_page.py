from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SETTING_BUTTON =( By.XPATH, "//a[@href='https://soft.reelly.io/settings' and @data-sentry-component='LinkWrapper']")       #(By.XPATH, "//a[@href='/settings' and contains(@class,'menu-button-block')]")



    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')

    def click_setting(self):
        self.wait_until_element_present(*self.SETTING_BUTTON)
        self.click(*self.SETTING_BUTTON)
