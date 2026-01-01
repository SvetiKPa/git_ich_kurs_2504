import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_drag_and_drop(driver):
    """Тест drag-and-drop функциональности"""
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    sleep(3)

    # Переключаемся в iframe
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
    driver.switch_to.frame(iframe)

    # Находим элементы
    photo = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]")
    trash = driver.find_element(By.ID, "trash")

    # Выполняем drag-and-drop
    actions = ActionChains(driver)
    actions.drag_and_drop(photo, trash).perform()
    sleep(2)

    # Проверяем результат
    photos_in_trash = len(driver.find_elements(By.XPATH, "//div[@id='trash']//li"))
    photos_in_gallery = len(driver.find_elements(By.XPATH, "//ul[@id='gallery']/li"))

    assert photos_in_trash == 1
    assert photos_in_gallery == 3
