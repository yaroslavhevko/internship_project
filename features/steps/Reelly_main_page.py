from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait


@when('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Click on the setting option')
def click_setting(context):
    context.app.main_page.click_setting()
