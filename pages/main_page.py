from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SETTING_BUTTON =(By.XPATH,'//a[@href="/settings"]')


    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')

    def click_setting(self):
        self.click(*self.SETTING_BUTTON)
        self.wait_until_element_present(*self.SETTING_BUTTON)