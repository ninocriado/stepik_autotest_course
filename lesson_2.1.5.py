from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

m = browser.find_element(By.ID, "answer")
m.send_keys(y)

n = browser.find_element(By.ID, "robotCheckbox")
n.click()

p = browser.find_element(By.ID, "robotsRule")
p.click()

button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
button.click()

time.sleep(20)
browser.quit()
