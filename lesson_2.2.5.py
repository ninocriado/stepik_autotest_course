from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element(By.NAME, 'firstname').send_keys("Ivan")
input2 = browser.find_element(By.NAME, 'lastname')
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, 'email')
input3.send_keys("smolensk@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
path = browser.find_element(By.NAME, "file")
path.send_keys(file_path)

button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
button.click()

time.sleep(20)
browser.quit()
