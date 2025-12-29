import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_checkout_total(driver):
    # 1. Логин
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # 2. Добавить товары
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.add_bolt_tshirt()
    inventory.add_onesie()
    inventory.go_to_cart()

    # 3. Оформить заказ
    cart = CartPage(driver)
    cart.checkout()
    cart.fill_form("John", "Doe", "12345")

    # 4. Проверить сумму
    total = cart.get_total()
    assert total == "58.29", f"Итог: ${total}, ожидалось: $58.29"
    print(f"Total: ${total}")