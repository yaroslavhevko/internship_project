from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingPage(Page):
    COMMUNITY_BTN =(By.XPATH,"//a[@href='/community' and .//div[normalize-space()='Community']]")     #(By.CSS_SELECTOR,'a[href="/community"]') for web
    #NEWS_BTN =(By.XPATH,"//a[@href='https://t.me/reellydxb' and .//div[normalize-space()='News']]")

    def click_community(self):
        self.scroll(self.COMMUNITY_BTN)
        self.wait_until_clickable(*self.COMMUNITY_BTN)
        self.click(*self.COMMUNITY_BTN)
       # from time import sleep
       # sleep(5)