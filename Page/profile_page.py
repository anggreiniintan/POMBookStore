from time import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class ProfilePage():
    #LOCATOR
    DASHBOARD_USERINFO = (By.ID, "userName-value")
    GO_BOOKSTORE = (By.ID, "gotoStore")
    DELETE_ALL_BOOKS = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[3]/button[1]")
    MODAL = (By.CLASS_NAME, "class='modal-content'")
    MODAL_OK = (By.ID, "closeSmallModal-ok")
    MODAL_CANCEL = (By.ID, "closeSmallModal-cancel")
    
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

    def click_delete_allbooks(self):
        self.driver.execute_script("window.scrollTo(0, 450)")
        delete_allbooks = self.driver.find_element(*self.DELETE_ALL_BOOKS)
        delete_allbooks.click()

    def modal_delete_allbooks(self):
        #want to delete all books
        # modal = self.driver.find_element(*self.MODAL)
        confirm_delete = self.driver.find_element(*self.MODAL_OK)
        confirm_delete.click()

    def modal_cancel_delete(self):
        #want to cancel delete all books
        cancel_delete = self.driver.find_element(*self.MODAL_CANCEL)
        cancel_delete.click()

   