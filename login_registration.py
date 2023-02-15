import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
email = driver.find_element_by_xpath('//input[@name="email"]')
email.click()
email.send_keys("smellsliketeen@spirit.ru")
password = driver.find_element_by_xpath('//input[@id="reg_password"]')
password.click()
password.send_keys("Kurt123456!")
driver.find_element_by_css_selector(".woocomerce-FormRow .woocommerce-Button").click()
driver.quit()