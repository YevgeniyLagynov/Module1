from selenium import webdriver
from time import sleep
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    listOfInputs = browser.find_elements_by_xpath("//input[@type='text']")
    for input in listOfInputs:
        input.send_keys('blablabla')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file1.txt')
    fileInput = browser.find_element_by_xpath("//input[@type='file']")
    fileInput.send_keys(file_path)


    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()


finally:
    sleep(10)
    browser.quit()

