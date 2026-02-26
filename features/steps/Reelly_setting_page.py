from behave import given, when, then

@when('Click on the Community option')
def click_community(context):
    from time import sleep
    sleep(10)
    context.app.setting_page.click_community()
