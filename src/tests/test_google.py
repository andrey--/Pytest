from selenium import webdriver

def test_google():
    driver=webdriver.Chrome()
    driver.get("http://google.com")
    assert "Google" in driver.page_source
    driver.quit()