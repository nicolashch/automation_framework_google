from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# class that defines one page of the site
class GoogleSearch:
    SEARCH_INPUT = (By.NAME, 'q')
    FIRST_RESULT = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Main_Page"]')

    # Constructor method
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.url = "{}".format(config['environment']['url'])

    # Go to the site
    def load(self):
        self.driver.get(self.url)

    # Get the title from the site you're current at
    def title(self):
        return self.driver.title

    # Take a Screenshot of the current view
    def take_screenshot(self, custom_name=None):
        pass

    # Identifies search bar element, types in it and send input
    def search_input(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys("Wikipedia" + Keys.ENTER)
        return self.driver, self.config

    def click_on(self):
        click_on = self.driver.find_element(*self.FIRST_RESULT)
        click_on.click()
        return self.driver, self.config
