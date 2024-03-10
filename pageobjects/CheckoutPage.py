import allure
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage
from pageobjects.Header import Header
from pageobjects.ThankYouPage import ThankYouPage
from pageobjects.products.AbstractCardPage import AbstractCardPage


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        super().wait_for_element_displayed(Locators.SHOPPING_FORM)
        self.header = Header(driver)
        self.total = self.find_element(Locators.PRODUCT_TOTAL).text

    @allure.step("Assert product price in checkout page")
    def assert_total_price(self, product: AbstractCardPage):
        logging.info("Asserting produce price in cart")
        assert product.product_price == self.total, \
            f'\nexpected price was: {product.product_price}\nactual price is {self.total}'
        return self

    @allure.step("Filling data in at Checkout page")
    def fill_user_data(self):
        logging.info("Start filling user data")
        logging.info("Set Full name as 'TEST NAME'")
        self.find_element(Locators.FULL_NAME_INPUT).send_keys("TEST NAME")
        self.find_element(Locators.ADDRESS_INPUT).send_keys("TEST ADDRESS")
        self.find_element(Locators.POSTAL_INPUT).send_keys("123456")
        self.find_element(Locators.CITY_INPUT).send_keys("TEST CITY")
        self.find_element(Locators.PHONE_INPUT).send_keys("987654321")
        self.find_element(Locators.EMAIL_INPUT).send_keys("test@test.test")
        self.select_value_from_dropdown_by_text(Locators.COUNTRY_SELECT, "Afghanistan - AF")
        return self

    @allure.step("Confirm order")
    def confirm_order(self) -> ThankYouPage:
        logging.info("Clicking 'Place order' button at checkout page")
        ActionChains(self.driver).move_to_element(self.find_element(Locators.PLACE_ORDER_BUTTON)).click().perform()
        return ThankYouPage(self.driver)


class Locators:
    SHOPPING_FORM = (By.XPATH, "//div[@id='shopping-cart-submit-container']")
    PRODUCT_TOTAL = (By.XPATH, "//td[@class='td-total']")

    INPUT_PLACEHOLDER = "//input[@name='<NAME>']"
    FULL_NAME_INPUT = (By.XPATH, INPUT_PLACEHOLDER.replace("<NAME>", "cart_name"))
    ADDRESS_INPUT = (By.XPATH, INPUT_PLACEHOLDER.replace("<NAME>", "cart_address"))
    POSTAL_INPUT = (By.XPATH, INPUT_PLACEHOLDER.replace("<NAME>", "cart_postal"))
    CITY_INPUT = (By.XPATH, INPUT_PLACEHOLDER.replace("<NAME>", "cart_city"))
    PHONE_INPUT = (By.XPATH, INPUT_PLACEHOLDER.replace("<NAME>", "cart_phone"))
    EMAIL_INPUT = (By.XPATH, INPUT_PLACEHOLDER.replace("<NAME>", "cart_email"))
    COUNTRY_SELECT = (By.XPATH, "//select[@name='cart_country']")

    PLACE_ORDER_BUTTON = (By.XPATH, "//input[@value='Place Order']")

