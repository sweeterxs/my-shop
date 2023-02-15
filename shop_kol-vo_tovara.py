import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
email = driver.find_element_by_xpath('//input[@name="username"]')
email.click()
email.send_keys("smellsliketeen@spirit.ru")
password = driver.find_element_by_xpath('//input[@id="password"]')
password.click()
password.send_keys("Kurt123456!")
driver.find_element_by_css_selector(".form-row .woocommerce-Button").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector(".cat-item.cat-item-19 :nth-child(1)").click()
items = driver.find_elements_by_css_selector(".products.masonry-done .product.type-product")
if len(items) == 3:
    print ("Отображается 3 товара")
else:
    print("Ошибка. Доступно товаров:" + str(len(items)))
driver.quit()