from selenium.webdriver.common.by import By


class GoogleSearch:
    SEARCH_INPUT = (By.ID, 'q')

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.url = "{}".format(config['environment']['url'])
