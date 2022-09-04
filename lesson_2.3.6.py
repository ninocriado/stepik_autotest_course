import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

knopka = browser.find_element(By.CLASS_NAME, "trollface")
knopka.click()

window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

f = browser.find_element(By.ID, "input_value")
x = f.text
y = calc(x)
pole = browser.find_element(By.ID, "answer")
pole.send_keys(y)
button = browser.find_element(By.CLASS_NAME, "btn-primary")
button.click()

time.sleep(10)

time.sleep(10)
