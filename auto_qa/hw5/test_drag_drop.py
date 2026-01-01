from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://www.globalsqa.com/demo-site/draganddrop/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

sleep(3)


# Переключение в iframe с изображениями
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

photo = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]")
# Первая фотография
trash = driver.find_element(By.ID, "trash")

# Выполняем drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(photo, trash).perform()
sleep(2)


# Проверяем количество фотографий в корзине и на основной панели
photos_in_trash = len(driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li"))
photos_in_gallery = len(driver.find_elements(By.XPATH, "//ul[@id='gallery']/li"))

assert photos_in_trash == 1, "Ошибка: В корзине нет фотографий!"
assert photos_in_gallery == 3, "Ошибка: В основной области осталось не 3 фотографии!"

print("Тест успешно пройден: Фотография перемещена в корзину, в галерее осталось 3 фотографии.")
driver.quit()

