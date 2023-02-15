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
driver.implicitly_wait(3)
driver.find_element_by_css_selector(".checkout-button.button.alt.wc-forward").click()
driver.implicitly_wait(3)
name = driver.find_element_by_xpath('//input[@id="billing_first_name"]')
name.click()
name.send_keys("Kurt")
last_name = driver.find_element_by_xpath('//input[@id="billing_last_name"]')
last_name.click()
last_name.send_keys("Cobain")
email = driver.find_element_by_xpath('//input[@id="billing_email"]')
email.click()
email.send_keys("smellsliketeen@spirit.ru")
phone = driver.find_element_by_xpath('//input[@id="billing_phone"]')
phone.click()
phone.send_keys("89006660066")
driver.find_element_by_css_selector(".select2-arrow").click()
country = driver.find_element_by_xpath('//input[@id="s2id_autogen1_search"]')
country.send_keys("Jamaica")
driver.find_element_by_css_selector(".select2-match").click()
street = driver.find_element_by_xpath('//input[@id="billing_address_1"]')
street.click()
street.send_keys("Test Str.")
town = driver.find_element_by_xpath('//input[@id="billing_city"]')
town.click()
town.send_keys("Betester")
state = driver.find_element_by_xpath('//input[@id="billing_state"]')
state.click()
state.send_keys("Automation")
zip = driver.find_element_by_xpath('//input[@id="billing_postcode"]')
zip.click()
zip.send_keys("666696")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector(".payment_method_cheque .input-radio").click()
driver.find_element_by_css_selector(".place-order .button.alt").click()
driver.implicitly_wait(3)
thx = driver.find_element_by_css_selector(".woocommerce-thankyou-order-received")
thx_check = thx.text
assert thx_check == "Thank you. Your order has been received."
pay = driver.find_element_by_css_selector(".shop_table.order_details tfoot :nth-child(3) td")
pay_check = pay.text
assert pay_check == "Check Payments"
driver.quit()

