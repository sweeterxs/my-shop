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
driver.find_element_by_xpath('//img[@title="Android Quick Start Guide"]').click()
last=driver.find_element_by_css_selector("del .woocommerce-Price-amount.amount")
last_price = last.text
assert last_price == "₹600.00"
now=driver.find_element_by_css_selector("ins .woocommerce-Price-amount.amount")
now_price = now.text
assert now_price == "₹450.00"
driver.implicitly_wait(3)
driver.find_element_by_xpath('//img[@title="Android Quick Start Guide"]').click()
driver.implicitly_wait(5)
driver.find_element_by_css_selector(".pp_close").click()
driver.quit()