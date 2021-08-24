from typing import FrozenSet
from selenium import webdriver
from Page.login_page import LoginPage
from Page.register_page import RegisterPage

class TestRegister():

    def test_register(self, browser: webdriver.Remote):
        #can't handle captcha
        login_page = LoginPage(browser)        
        register_page = RegisterPage(browser)
        login_page.load_website()
        login_page.button_newuser_click()
        register_page.set_fnm("harley")
        register_page.set_lnm("Davidson")
        register_page.set_username("hrlydvdsn")
        register_page.set_pw("1234567890Az@")
        register_page.button_register()
        
    
