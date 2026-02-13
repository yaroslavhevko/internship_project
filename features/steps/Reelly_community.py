from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait


@when('Verify the right page open')
def verify_right_page(context):
    context.app.community_page.verify_right_page()

@then('Verify the "Support" button is available and clickable')
def click_contact_support(context):
    context.app.community_page.click_contact_support()
def wait_until_windows_count_is(context):
    context.app.community_page.wait_until_windows_count_is()
def switch_to_newest_tab(context):
    context.app.community_page.switch_to_newest_tab()