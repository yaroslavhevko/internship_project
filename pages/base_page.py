from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_until_element_present(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by locator {locator}'
        )
    def wait_until_element_visible(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not visible by locator {locator}'
        )

    def wait_until_element_invisible(self, *locator):
        self.driver.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by locator {locator}'
        )

    def wait_until_clickable(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by locator {locator}'
        )

    def wait_until_clickable_click(self, *locator, timeout=10):
       # self.driver.wait.until(
       #     EC.element_to_be_clickable(locator),
      #     message=f'Element not clickable by locator {locator}'
       # ).click()
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def scroll(self, *locator, timeout=15):

        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script("arguments[0].click();", element)


    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text in actual_text,\
            f"Expected {expected_partial_text} not in actual {actual_text}"

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f"Expected {expected_text}, but got actual {actual_text}"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, \
            f"Expected {expected_url}, but got {actual_url}"

    def verify_url_contains(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f"Expected {expected_partial_url} not in {actual_url}"

    def wait_until_windows_count_is(self, expected_count: int):
        self.driver.wait.until(
            EC.number_of_windows_to_be(expected_count),
            message=f'Expected {expected_count} windows, but got {len(self.driver.window_handles)}'
        )

    def switch_to_newest_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])