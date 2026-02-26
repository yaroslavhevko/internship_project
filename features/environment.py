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
    context.driver = webdriver.Chrome()

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

   # bs_user = 'yaroslavhevkoqwf_DRiFwz'
   # bs_key = 'UUwoTzfmirZpRwsnvyzz'

   # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
   # options = Options()
   # bstack_options = {
   #     "os": "Windows",
   #     "osVersion": "10",
   #     "browserVersion": "latest",
   #     'browserName': 'Chrome',
   #     'sessionName': scenario_name,
   # }
   # options.set_capability('bstack:options', bstack_options)
  #  context.driver = webdriver.Remote(command_executor=url, options=options)

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
