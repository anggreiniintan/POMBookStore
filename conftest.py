from selenium import webdriver
import pytest
import time

@pytest.fixture
def browser():
    path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
    browser = webdriver.Chrome(executable_path = path)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    time.sleep(5)
    browser.close()