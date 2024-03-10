import allure
import pytest
from selenium.webdriver.android.webdriver import WebDriver

from pageobjects.MainPage import MainPage


@pytest.mark.smoke
@allure.parent_suite("End-to-End tests")
@allure.suite("End-to-End test for table purchasing")
@allure.title("Purchase random table")
def test_e2e_table_purchase(driver: WebDriver):
    product = MainPage(driver).open_page() \
        .open_tables_page() \
        .open_random_card_page()

    product.add_product_to_cart() \
        .assert_product_added_message_displayed() \
        .open_cart_page() \
        .assert_total_price(product) \
        .place_order() \
        .assert_total_price(product) \
        .fill_user_data() \
        .confirm_order() \
        .assert_thank_you_sign_is_displayed()
