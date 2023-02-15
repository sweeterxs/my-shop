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
log_out=driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout :nth-child(1)")
log_out1 = log_out.get_attribute("href")
if log_out1 is not True:
    print ('Элемент "Logout" найден')
else:
    print ('Элемент "Logout" не найден')
driver.quit()