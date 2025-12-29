from selenium.webdriver.common.by import By
from time import sleep

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fill_form(self, first_name, last_name, zip_code):
        """Заполняем форму на странице оформления заказа"""
        # Без пауз "падает"
        sleep(1)
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()
        # Без пауз "падает"
        sleep(1)

    def get_total(self):
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        # "Total: $58.29" -> "58.29"
        return total_text.split("$")[1]