from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class RegisterPage():
    #LOCATOR
    FNM = (By.ID, "firstname")
    LNM = (By.ID, "lastname")
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    BUTTON_REGISTER = (By.ID, "register")    
    
    #Method Constuctor
    def __init__(self, browser: webdriver.Remote):
        self.driver = browser
    
    def set_fnm(self, fnm):
        fnm_field = self.driver.find_element(*self.FNM)
        fnm_field.send_keys(fnm)
    
    def set_lnm(self, lnm):
        lnm_field = self.driver.find_element(*self.LNM)
        lnm_field.send_keys(lnm)
    
    def set_username(self, username):
        username_field = self.driver.find_element(*self.USERNAME)
        username_field.send_keys(username)
    
    def set_pw (self, pw):
        pw_field = self.driver.find_element(*self.PASSWORD)
        pw_field.send_keys(pw)

    def button_register(self):
        self.driver.execute_script("window.scrollTo(0, 250)") 
        newuser_button = self.driver.find_element(*self.BUTTON_REGISTER)
        newuser_button.click()

   