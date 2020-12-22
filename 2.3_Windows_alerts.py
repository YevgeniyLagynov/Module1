from selenium import webdriver
from time import sleep
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    # confirm1 = browser.switch_to.alert
    # confirm1.accept()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)



    x = browser.find_element_by_id('input_value').text
    result = calc(x)
    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_xpath('//button').click()




finally:
    sleep(10)
    browser.quit()