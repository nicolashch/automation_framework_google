import sys
sys.path.append('./pages')
sys.path.append('./libs')

import os
import json
import pytest
import logging
import validators
#import datetimecd
import selenium.webdriver
from constants import SUPPORTED_BROWSERS


LOGGER = logging.getLogger(__name__)
_driver = None


@pytest.fixture
def web_browser(config):
    global _driver
    browser_name = config['config']['browser']['name'].lower()
    if config['config']['use_grid']:
        _driver = initialize_remote_driver(browser_name, config['config']['grid'])
    else:
        _driver = initialize_local_driver(browser_name, config['config']['browser']['executable_path'])

    _driver.implicitly_wait(config['config']['implicit_wait'])
    _driver.set_window_size(1800, 900)
    # _driver.maximize_window()
    _driver.delete_all_cookies()
    yield _driver
    _driver.quit()


# The fixture is destroyed at the end of the test.
@pytest.fixture(scope='function')
def context():
    return {}


@pytest.fixture
def config(scope="session"):
    with open('config.json') as configFile:
        config = json.load(configFile)

    assert isinstance(config['config']['use_grid'], bool), \
        "{} Must be a Boolean".format(config['config']['use_grid'])
    assert validators.url(config['config']['grid']), \
        "{} Must be a valid url".format(config['config']['grid'])
    assert config['config']['browser']['name'].lower() in SUPPORTED_BROWSERS, \
        "{} Must be one of '{}'".format(config['config']['browser']['name'], SUPPORTED_BROWSERS)
    assert isinstance(config['config']['implicit_wait'], int), \
        "{} Must be a number".format(config['config']['implicit_wait'])
    assert validators.url(config['environment']['url']), \
        "{} Must be a valid url".format(config['environment']['url'])

    return config


def initialize_remote_driver(browser_name, grid_url, options=None):
    LOGGER.info("Web Driver [ {} ] using [ Selenium Grid ]".format(browser_name))

    if browser_name == 'chrome':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            # options=options,
            desired_capabilities={
                'browserName': 'chrome',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'firefox':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            # options=options,
            desired_capabilities={
                'browserName': 'firefox',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'safari':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            # options=options,
            desired_capabilities={
                'browserName': 'operablink',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'edge':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            # options=options,
            desired_capabilities={
                'browserName': 'MicrosoftEdge',
                'acceptInsecureCerts': True
            })
    return driver


def initialize_local_driver(browserName, executable_path, options=None):
    LOGGER.info("Web Driver [ {} ] using [ Local Environment ]".format(browserName))

    if browserName == 'chrome':
        driver = selenium.webdriver.Chrome(
            # options=options,
            executable_path=executable_path)
    elif browserName == 'firefox':
        driver = selenium.webdriver.Firefox(
            # options=options,
            executable_path=executable_path)
    elif browserName == 'safari':
        driver = selenium.webdriver.Safari(
            # options=options,
            executable_path=executable_path)
    elif browserName == 'edge':
        driver = selenium.webdriver.Edge(
            # options=options,
            executable_path=executable_path)
    return driver
