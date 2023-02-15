import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector(".post-160 .button.product_type_simple").click()
driver.find_element_by_class_name('reviews_tab').click()
driver.find_element_by_class_name("star-5").click()
rewiew = driver.find_element_by_tag_name('textarea')
rewiew.click()
rewiew.send_keys("Nice book!")
name = driver.find_element_by_xpath('//input[@name="author"]')
name.click()
name.send_keys("Kurt")
email = driver.find_element_by_xpath('//input[@name="email"]')
email.click()
email.send_keys("smellsliketeen@spirit.ru")
driver.find_element_by_css_selector(".form-submit  .submit").click()
driver.quit()