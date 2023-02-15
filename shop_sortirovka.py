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
element = driver.find_element_by_css_selector(".orderby :nth-child(6)")
status0 = element.get_attribute("selected")
if status0 is not True:
    print ('Сортировка по умолчанию')
else:
    print ('Сортировка не по умолчанию!')
from selenium.webdriver.support.select import Select
element1 = driver.find_element_by_xpath('//select[@name="orderby"]')
select = Select(element1) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_value("price-desc")
sorter = driver.find_element_by_css_selector(".orderby :nth-child(6)")
status1 = sorter.get_attribute("selected")
if status1 is not True:
    print ('Сортировка по убыванию цены')
else:
    print ('Неверный тип сортировки!')
driver.quit()