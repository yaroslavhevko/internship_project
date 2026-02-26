from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SETTING_BUTTON =( By.CSS_SELECTOR, "a[href*='/settings'] span.font-medium.whitespace-nowrap")       #(By.XPATH, "//a[@href='/settings' and contains(@class,'menu-button-block')]")


    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')


    def click_setting(self):
       # self.scroll(*self.SETTING_BUTTON)
        self.wait_until_element_present(*self.SETTING_BUTTON)
        self.click(*self.SETTING_BUTTON)
       # sleep(10)