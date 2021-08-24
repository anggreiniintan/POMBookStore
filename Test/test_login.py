from Page import register_page
from selenium import webdriver
from Page.login_page import LoginPage
from Test.test_register import TestRegister

class TestLogin():
    def test_valid_login(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        login_page.load_website()
        login_page.set_username("as")
        login_page.set_pw("intaN21@")
        login_page.button_signin_click()

        assert login_page.get_userinfo_name() == "as"

    

    
