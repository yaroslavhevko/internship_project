from pages.sign_in_page import SignInPage
from pages.main_page import MainPage
from pages.setting_page import SettingPage
from pages.community_page import CommunityPage
class Application:

    def __init__(self,driver):

        self.sign_in_page = SignInPage(driver)
        self.main_page = MainPage(driver)
        self.setting_page = SettingPage(driver)
        self.community_page = CommunityPage(driver)