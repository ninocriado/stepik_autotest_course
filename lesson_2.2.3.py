from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

first = browser.find_element(By.ID, "num1")
x = first.text

second = browser.find_element(By.ID, "num2")
y = second.text

z = str(int(x) + int(y))

menu = Select(browser.find_element(By.ID, "dropdown"))
menu.select_by_value(z)

button = browser.find_element(By.CLASS_NAME, "btn-default")
button.click()

time.sleep(20)
browser.quit()


