from Test.test_profile import TestProfile
from Page.bookstore_page import BookStorePage
from selenium import webdriver

class TestBookStore():
    def test_get_tittle_book(self, browser: webdriver.Remote):
        profile_page = TestProfile()    
        bookstore_page = BookStorePage(browser)    
        profile_page.test_go_to_bookstore(browser)
        bookstore_page.get_text_choosebook()
