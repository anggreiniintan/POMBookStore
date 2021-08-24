from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from Page.profile_page import ProfilePage
from Test.test_login import TestLogin

class TestProfile():
   def test_go_to_bookstore(self, browser: webdriver.Remote):
       profile_page = ProfilePage(browser)
       test_login = TestLogin()
       test_login.test_valid_login(browser)
       profile_page.click_go_bookstore()