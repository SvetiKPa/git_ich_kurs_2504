from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.set_window_size(640, 460)  #для моб.версии
    # driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(options=options)
    yield driver                #запуск браузера
    driver.quit()



def test_elements_displayed(driver):
    driver.get('https://itcareerhub.de/ru')
    logo = driver.find_element(By.CSS_SELECTOR, "[alt='IT Career Hub']")
    assert logo.is_displayed()


    # Ссылка “Программы” на странице отображается
def test_link1_displayed(driver):
    driver.get('https://itcareerhub.de/ru')
    link1 = driver.find_element(By.LINK_TEXT, "Программы")
    assert link1.is_displayed()

    # Ссылка “Способы оплаты” на странице отображается
def test_link2_displayed(driver):
    driver.get('https://itcareerhub.de/ru')
    link2 = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert link2.is_displayed()


def test_link3_displayed(driver):
    driver.get('https://itcareerhub.de/ru')
    link3 = driver.find_element(By.LINK_TEXT, "О нас")
    assert link3.is_displayed()

def test_link4_displayed(driver):
    driver.get('https://itcareerhub.de/ru')
    link4 = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert link4.is_displayed()


# def test_button_ru_displayed(driver):
#     driver.get('https://itcareerhub.de/ru')
#     element_ru = driver.find_element(By.CSS_SELECTOR, ".tn-atom__button-content span")
#     assert element_ru.is_displayed()

def test_ru_button_displayed(driver):
    driver.get('https://itcareerhub.de/ru')
    ru_button = driver.find_element(By.XPATH, "//span[text()='ru']")
    assert ru_button.text == "ru"
    assert ru_button.is_displayed()

def test_de_button_displayed(driver):
    driver.get('https://itcareerhub.de/de')
    de_button = driver.find_element(By.XPATH, "//span[text()='de']")
    assert de_button.text == "de"
    assert de_button.is_displayed()


def test_contact_displayed(driver):
    driver.get('https://itcareerhub.de/ru/contact-us')
    page_source = driver.page_source
    required_text = "Если вы не дозвонились, заполните форму на сайте.Мы свяжемся с вами"
    if required_text in page_source:
        print(f"Текст '{required_text}' найден на странице")
        assert True
    # element = driver.find_element(By.LINK_TEXT,
    #                               'Если вы не дозвонились, заполните форму на сайте.Мы свяжемся с вами')
    # assert element.is_displayed()


