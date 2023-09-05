from configparser import ConfigParser
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FfoxOpptions
from selenium.webdriver.firefox.service import Service as FfoxService


from selenium.webdriver.firefox.service import Service as FirefoxService


def get_root_directory():
    return os.path.split(__file__)[0]


def get_config():
    config = ConfigParser()
    config.read(os.path.join(get_root_directory(), 'config.ini'))
    return config


def get_base_url():
    return get_config().get('project', 'base_url')


def get_browser_name():
    return get_config().get('project', 'browser_name')


def get_driver():
    if get_browser_name().lower() == 'chrome':
        options = ChromeOptions()
        """Options for headless mode"""
        # options.add_argument('--headless')  # Use headless mode
        # options.add_argument('--disable-gpu')  # Disable GPU acceleration in headless mode
        # options.add_argument('--no-sandbox')  # Disable sandboxing in headless mode
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif get_browser_name().lower() == 'firefox':
        # Set up Firefox WebDriver options
        firefox_options = FfoxOpptions()
        service = FfoxService(executable_path=GeckoDriverManager().install())
        # Create the WebDriver using webdriver_manager
        driver = webdriver.Firefox(service=service, options=firefox_options)


    else:
        raise NotImplementedError

    return driver

