from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    """
    Driver path
    """
   # driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)


    """
    Headless Chrome
    """


    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #context.driver = webdriver.Chrome(options=options)

    """
    Headless Firefox
    """
    #context.driver = webdriver.Firefox()

    #options = webdriver.FirefoxOptions()
    #options.add_argument('--headless')
    #context.driver = webdriver.Firefox(options=options)
    """
    BrowserStack Mobile session
    """

    bs_user = 'yaroslavhevkoqwf_DRiFwz'
    bs_key = 'UUwoTzfmirZpRwsnvyzz'

    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    chrome_prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", chrome_prefs)
    bstack_options = {
        "os": "Android",
        "osVersion": "13.0",
        "deviceName": "Samsung Galaxy S23+",
        'browserName': 'Chrome',
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    mobile_emulation = {"deviceName": "Samsung Galaxy S8+"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=options)
    context.is_mobile = True



    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.quit()
