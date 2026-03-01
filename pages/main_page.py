from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SETTING_BUTTON =(By.XPATH, "//a[@href='/settings' and .//div[normalize-space()='Menu']]")                      #( By.CSS_SELECTOR, "a[href*='/settings'] span.font-medium.whitespace-nowrap") for web
    MARKET_OFFER_BTN= (By.XPATH, "//a[@href='https://soft.reelly.io/' and .//span[text()='Market Offers']]")

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')

    def click_market_offer(self):
        self.wait_until_element_present(*self.MARKET_OFFER_BTN)
        self.click(*self.MARKET_OFFER_BTN)


    def click_setting(self):
       # self.scroll(*self.SETTING_BUTTON)
        self.wait_until_element_present(*self.SETTING_BUTTON)
        self.click(*self.SETTING_BUTTON)
       # sleep(10)