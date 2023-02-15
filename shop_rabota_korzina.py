import time
from selenium.webdriver.common.by import By
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector(".post-165").click()
driver.find_element_by_css_selector(".single_add_to_cart_button.button.alt").click()
driver.implicitly_wait(3)
driver.find_element_by_css_selector(".button.wc-forward").click()
driver.find_element_by_css_selector(".remove").click()
driver.find_element_by_link_text("Undo?").click()
driver.find_element_by_css_selector(".input-text.qty.text").clear()
value = driver.find_element_by_css_selector(".input-text.qty.text")
value.clear()
value.click()
value.send_keys("3")
driver.find_element_by_css_selector(".actions :nth-child(2)").click()
value_check = value.text
assert value_check == "3"
driver.find_element_by_css_selector(".actions .coupon :nth-child(3)").click()
close_btn_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))
driver.quit()