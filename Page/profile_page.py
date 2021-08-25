from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class ProfilePage():
    #LOCATOR
    DASHBOARD_USERINFO = (By.ID, "userName-value")
    GO_BOOKSTORE = (By.ID, "gotoStore")
    
    
    #Method Constuctor
    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def get_userinfo_name(self):
        dashboard_username = self.driver.find_element(*self.DASHBOARD_USERINFO)
        return dashboard_username.text

    def click_go_bookstore(self):
        self.driver.execute_script("window.scrollTo(0, 450)")
        go_to_bookstore = self.driver.find_element(*self.GO_BOOKSTORE)
        go_to_bookstore.click()
   