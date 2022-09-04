from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

m = browser.find_element(By.ID, "answer")
m.send_keys(y)

n = browser.find_element(By.ID, "robotCheckbox")
n.click()

p = browser.find_element(By.ID, "robotsRule")
p.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(20)
browser.quit()