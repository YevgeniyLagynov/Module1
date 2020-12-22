from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time




try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)

    result = num1 + num2
    print(num1,num2,result)

    select =  Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(result))

    browser.find_element_by_xpath("//button").click()














finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
