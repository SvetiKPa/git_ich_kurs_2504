from selenium.webdriver.common.by import By
from time import sleep


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

        self.total_price_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, zip_code):
        """Заполнить форму на странице Checkout: Your Information"""
        sleep(1)
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        sleep(1)
        total_text = self.driver.find_element(*self.total_price_label).text

        # Пример текста: "Total: $58.29"
        if "Total: $" in total_text:
            return total_text.split("Total: $")[1]
        elif "$" in total_text:
            return total_text.split("$")[1]
        return total_text