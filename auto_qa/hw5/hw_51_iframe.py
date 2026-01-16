import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe_text(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))    )

    expected_text = "semper posuere integer et senectus justo curabitur."
    page_text = driver.find_element(By.TAG_NAME, "body").text
    found = expected_text in page_text
    driver.switch_to.default_content()
    assert found, "Текст не найден внутри iframe"