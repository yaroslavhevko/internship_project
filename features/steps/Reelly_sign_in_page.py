from selenium.webdriver.common.by import By
from behave import given, when, then
from config.config import EMAIL, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait


@given('Open Sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when('log in to page')
def log_in_to_page(context):
    context.app.sign_in_page.log_in_to_page(EMAIL, PASSWORD)

