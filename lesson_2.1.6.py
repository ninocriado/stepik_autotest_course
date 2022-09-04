from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

j = browser.find_element(By.ID, "treasure")
x = j.get_attribute("valuex")
print(x)
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