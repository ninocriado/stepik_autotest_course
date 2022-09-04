import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

knopka = browser.find_element(By.CLASS_NAME, "btn-primary")
knopka.click()

confirm = browser.switch_to.alert
confirm.accept()

v = browser.find_element(By.ID, "input_value")
x = v.text
y = calc(x)
pole = browser.find_element(By.CLASS_NAME, "form-control")
pole.send_keys(y)

button = browser.find_element(By.CLASS_NAME, "btn-primary")
button.click()

time.sleep(20)

