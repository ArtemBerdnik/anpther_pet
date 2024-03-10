from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.BasePage import BasePage
from pageobjects.Header import Header


class AbstractPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header = Header(driver)

    def open_tables_page(self):
        self.header.open_tables_page()
        # return TablesPage(self.driver)

    def open_cart_page(self):
        self.header.open_cart_page()
        # return CartPage(self.driver)