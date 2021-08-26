from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class LoginPage():
    #LOCATOR
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    BUTTON_SIGIN = (By.ID, "login")
    BUTTON_NEWUSER = (By.ID, "newUser")
    DASHBOARD_USERINFO = (By.ID, "userName-value")
    HEADER_LOGIN = (By.XPATH, "//div[contains(text(),'Login')]")

    
    #Method Constuctor
    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def load_website(self):
        self.driver.get("https://demoqa.com/login")

    def set_username(self, username):
        username_field = self.driver.find_element(*self.USERNAME)
        username_field.send_keys(username)
    
    def set_pw (self, pw):
        pw_field = self.driver.find_element(*self.PASSWORD)
        pw_field.send_keys(pw)

    def button_signin_click(self):
        sigin_button = self.driver.find_element(*self.BUTTON_SIGIN)
        sigin_button.click()

    def button_newuser_click(self):
        newuser_button = self.driver.find_element(*self.BUTTON_NEWUSER)
        newuser_button.click()

    def get_text_main_header(self):
        get_text = self.driver.find_element(*self.HEADER_LOGIN)
        return get_text.text