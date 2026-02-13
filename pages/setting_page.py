from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingPage(Page):
    COMMUNITY_BTN =(By.XPATH,'//a[@href="/community"]')


    def click_community(self):
        self.click(*self.COMMUNITY_BTN)