from behave import given, when, then

@when('Click on the Community option')
def click_community(context):
    context.app.setting_page.click_community()
