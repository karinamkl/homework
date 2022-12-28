from selenium import webdriver
from golem.core.utils import match_latest_executable_path
from golem import execution
from golem.webdriver import GolemChromeDriver

def my_custom_chrome_tablet_vertical(settings):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=820,1180")

    executable_path = settings['chromedriver_path']
    matched_executable_path = match_latest_executable_path(executable_path,
                                                           execution.testdir)
    return GolemChromeDriver(executable_path=matched_executable_path,
                             chrome_options=chrome_options)

def my_custom_chrome_phone(settings):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=390,844")

    executable_path = settings['chromedriver_path']
    matched_executable_path = match_latest_executable_path(executable_path,
                                                           execution.testdir)
    return GolemChromeDriver(executable_path=matched_executable_path,
                             chrome_options=chrome_options)

def my_custom_chrome_tablet_horizontal(settings):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1180,820")

    executable_path = settings['chromedriver_path']
    matched_executable_path = match_latest_executable_path(executable_path,
                                                           execution.testdir)
    return GolemChromeDriver(executable_path=matched_executable_path,
                             chrome_options=chrome_options)