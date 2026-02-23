from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CommunityPage(Page):
    SUPPORT_BUTTON =(By.CSS_SELECTOR, "a[target='_blank'][href*='api.whatsapp.com']"
                     )    #(By.XPATH, "//a[@target='_blank' and contains(@href,'api.whatsapp.com/send?phone=971502091446')]")

    def verify_right_page(self):
        self.verify_url('https://soft.reelly.io/community')
        self.verify_url_contains('community')

    def click_contact_support(self):
        self.wait_until_clickable_click(*self.SUPPORT_BUTTON)

    def wait_until_windows_count_is(self, expected_windows_count=2):
        super().wait_until_windows_count_is(expected_windows_count)


    def switch_to_newest_tab(self):
        super().switch_to_newest_tab()