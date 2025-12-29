from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def setup_ru_site(driver):
    """Фикстура для открытия русской версии сайта"""
    driver.get('https://itcareerhub.de/ru')
    yield driver


@pytest.fixture
def setup_de_site(driver):
    """Фикстура для открытия немецкой версии сайта"""
    driver.get('https://itcareerhub.de/de')
    yield driver


def test_logo_is_displayed(setup_ru_site):
    driver = setup_ru_site
    logo = driver.find_element(By.CSS_SELECTOR, "[alt='IT Career Hub']")
    assert logo.is_displayed()


def test_programs_link_is_displayed(setup_ru_site):
    driver = setup_ru_site
    link = driver.find_element(By.LINK_TEXT, "Программы")
    assert link.is_displayed()


def test_payment_methods_link_is_displayed(setup_ru_site):
    driver = setup_ru_site
    link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert link.is_displayed()


# def test_news_link_is_displayed(setup_ru_site):
#     driver = setup_ru_site
#     link = driver.find_element(By.LINK_TEXT, "Новости")
#     assert link.is_displayed()
#
def test_blog_link_is_displayed(setup_ru_site):
    driver = setup_ru_site
    # link = driver.find_element(By.LINK_TEXT, "Блог")
    element = driver.find_element(By.ID, "molecule-176285426165558590")
    assert element.is_displayed()



def test_about_us_link_is_displayed(setup_ru_site):
    driver = setup_ru_site
    # link = driver.find_element(By.LINK_TEXT, "О нас")
    link = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590")
    assert link.is_displayed()


def test_reviews_link_is_displayed(setup_ru_site):
    driver = setup_ru_site
    link = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert link.is_displayed()


def test_ru_button_is_displayed(setup_ru_site):
    driver = setup_ru_site
    ru_element = driver.find_element(By.CSS_SELECTOR, "#rec1345258281")
    assert ru_element.is_displayed()


def test_de_button_is_displayed(setup_de_site):
    driver = setup_de_site
    de_element = driver.find_element(By.CSS_SELECTOR, "#rec1427921581")
    assert de_element.is_displayed()


