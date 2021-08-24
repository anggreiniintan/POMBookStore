from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class BookStorePage():
    # LOCATOR
    CHOOSE_BOOK = (By.ID, "see-book-Git Pocket Guide")

    #Method Constuctor
    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def get_text_choosebook(self):
        book = self.driver.find_element(*self.CHOOSE_BOOK)
        book.click()