import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager


@pytest.fixture()
@allure.title("Prepare for the test: Browser set up")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager(cache_manager=DriverCacheManager(valid_range=-1)).install())
    driver.maximize_window()
    yield driver
    driver.quit()
