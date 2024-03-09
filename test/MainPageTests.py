import allure
import pytest
from selenium.webdriver.android.webdriver import WebDriver

from pageobjects.MainPage import MainPage


@pytest.mark.parametrize("product_name", ["retro lamp7", "chair"])
@pytest.mark.smoke
@allure.suite("Tests for search")
@allure.title("Test search functionality in 'Main' page for {product_name}")
@allure.parent_suite("Tests for 'Main' page")
def test_search_positive(driver: WebDriver, product_name: str):
    main_page = MainPage(driver).open_page()
    main_page.assert_main_categories_displayed()
    main_page.type_to_search_input(product_name)
    main_page.assert_search_result(product_name)


@pytest.mark.regression
@allure.suite("Tests for search")
@allure.title("Test search functionality for non existing product")
@allure.parent_suite("Tests for 'Main' page")
def test_negative(driver: WebDriver):
    main_page = MainPage(driver).open_page()
    main_page.assert_main_categories_displayed()
    main_page.type_to_search_input("non_existing_product")
    main_page.assert_search_result_is_empty()
