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
driver.find_element_by_xpath('//img[@title="Mastering JavaScript"]').click()
driver.find_element_by_css_selector(".single_add_to_cart_button.button.alt").click()
driver.find_element_by_css_selector(".button.wc-forward").click()
driver.implicitly_wait(3)
subtotal=driver.find_element_by_css_selector(".cart-subtotal .woocommerce-Price-amount.amount")
subtotal_price = subtotal.text
assert subtotal_price == "₹350.00"
total=driver.find_element_by_css_selector(".product-subtotal .woocommerce-Price-amount.amount")
total_price = total.text
assert total_price == "₹350.00"
driver.quit()
