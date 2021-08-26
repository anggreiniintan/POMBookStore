from Page.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from Page.profile_page import ProfilePage
from Test.test_login import TestLogin
from Page.bookstore_page import BookStorePage

class TestProfile():
   def test_go_to_bookstore(self, browser: webdriver.Remote):
       profile_page = ProfilePage(browser)
       bookstore_page = BookStorePage(browser)
       test_login = TestLogin()
       test_login.test_valid_login(browser)
       profile_page.click_go_bookstore()

       assert bookstore_page.get_tittle_header() == "Book Store"
  
   def test_searchBox(self, browser: webdriver.Remote):
       profile_page = ProfilePage(browser)
       bookstore_page = BookStorePage(browser)
       test_login = TestLogin()
       test_login.test_valid_login(browser)
       profile_page.click_go_bookstore()
       bookstore_page.search_box()

       assert bookstore_page.search_result() == "Learning JavaScript Design Patterns"

   def test_delete_allbooks(self, browser: webdriver.Remote):
       profile_page = ProfilePage(browser)
       alert = BookStorePage(browser)
       test_login = TestLogin()
       test_login.test_valid_login(browser)
       profile_page.click_delete_allbooks()
       profile_page.modal_delete_allbooks()
       
       assert alert.get_alerttext() == "All Books deleted."

   def test_cancel_delete_allbooks(self, browser: webdriver.Remote):
       profile_page = ProfilePage(browser)
       test_login = TestLogin()
       test_login.test_valid_login(browser)
       profile_page.click_delete_allbooks()
       profile_page.modal_cancel_delete()

   def test_logout(self, browser: webdriver.Remote):
       profile_page = ProfilePage(browser)
       login_page = LoginPage(browser)
       test_login = TestLogin()
       test_login.test_valid_login(browser)
       profile_page.logout() 

       assert login_page.get_text_main_header() == "Login"

    

       

