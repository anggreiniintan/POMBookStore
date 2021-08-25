from Test.test_profile import TestProfile
from Page.bookstore_page import BookStorePage
from selenium import webdriver

class TestBookStore():
    def test_choosebook(self, browser: webdriver.Remote):
        profile_page = TestProfile()    
        bookstore_page = BookStorePage(browser)    
        profile_page.test_go_to_bookstore(browser)
        bookstore_page.choosebook()
        bookstore_page.add_to_collection()
        # bookstore_page.get_alerttext()

        assert bookstore_page.get_alerttext() == "Book added to your collection."


