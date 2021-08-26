from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

import time

class BookStorePage():
    # LOCATOR
    CHOOSE_BOOK = (By.ID, "see-book-Git Pocket Guide")
    AFTER_CHOOSE_BOOK = (By.XPATH, "//label[contains(text(),'Git Pocket Guide')]")
    ADD_TO_COLLECTION =(By.XPATH, "//button[contains(text(),'Add To Your Collection')]")

    #Method Constuctor
    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def choosebook(self):
        book = self.driver.find_element(*self.CHOOSE_BOOK)
        book.click()

    def get_tittle_choosebook(self):
        book_tittle = self.driver.find_element(*self.CHOOSE_BOOK)
        return book_tittle.text

    def get_tittle_after_choosebook(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Git Pocket Guide')]"))
            )
        finally:
            after = self.driver.find_element(*self.AFTER_CHOOSE_BOOK)
            return after.text

    def add_to_collection(self):
        self.driver.execute_script("window.scrollTo(0, 250)") 
        
        self.driver.find_element(*self.ADD_TO_COLLECTION).click() 
        
        
    
    def get_alerttext(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
            alert = self.driver.switch_to.alert
            return alert.text
            # print("alert accepted")
        except TimeoutException:
            print("no alert")
        