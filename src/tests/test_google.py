import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestGoogleSearch:
    @pytest.yield_fixture(scope="module")
    def driver_initialization(self):
        driver = webdriver.Chrome()
        driver.get("http://google.com")
        yield driver
        driver.quit()

    def test_google(self, driver_initialization):
        assert "Google" in driver_initialization.page_source
        driver_initialization.find_element_by_xpath("//input[@name='q']")
        driver_initialization.find_element_by_name("q")
# //*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input