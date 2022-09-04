from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("ivan.petrov@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
    input4.send_keys("89998887766")
    input5 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    input5.send_keys("Russia,Moscow")
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    time.sleep(20)
    browser.quit()

