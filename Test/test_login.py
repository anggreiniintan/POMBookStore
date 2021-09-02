from Page import register_page
from selenium import webdriver
from Page.login_page import LoginPage
from Page.profile_page import ProfilePage

class TestLogin():
       def test_valid_login(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)        
        login_page.load_website()
        login_page.set_username("as")
        login_page.set_pw("intaN21@")
        login_page.button_signin_click()

        assert profile_page.get_userinfo_name() == "as"

       def test_notvalid_login(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)    
        login_page.load_website()
        login_page.set_username("a")
        login_page.set_pw("intaN21@")
        login_page.button_signin_click()

        assert login_page.output_invalid_login() == "Invalid username or password!"

    

    
