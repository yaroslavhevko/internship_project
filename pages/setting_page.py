from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingPage(Page):
    COMMUNITY_BTN =(By.CSS_SELECTOR,'a[href="/community"]')


    def click_community(self):
        self.wait_until_clickable(*self.COMMUNITY_BTN)
        self.click(*self.COMMUNITY_BTN)