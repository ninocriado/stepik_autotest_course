import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestAbs(unittest.TestCase):

    def test1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

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

        theend = browser.find_element(By.TAG_NAME, "h1").text
        print(theend)
        self.assertEqual(theend, "Congratulations! You have successfully registered!")

        time.sleep(5)

    def test2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input2.send_keys("ivan.petrov@mail.ru")
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
        input3.send_keys("89998887766")
        input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
        input4.send_keys("Russia,Moscow")
        button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        button.click()

        theend = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(theend, "Congratulations! You have successfully registered!")
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()