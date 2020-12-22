from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = 'https://hotline.ua/'
    browser.get(link)
    inputField = browser.find_element_by_id('searchbox')
    inputField.send_keys('iPhone 7')
    inputButton = browser.find_element_by_id('doSearch')
    inputButton.click()
    #выбираем именно телефоны, а не акссесуары
    onlyPhones = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Смартфоны и мобильные телефоны')]"))
    )
    onlyPhones.click()

    #сортировка по возрастанию цены(от дешевых к дорогим)
    sortButton = browser.find_element_by_xpath("//div[@data-navigation-id='app-sorting']//select[@name='sort']")
    sortButton.click()

    sortFromLowToUp = browser.find_element_by_xpath("//option[contains(text(),'возрастанию цены')]")
    sortFromLowToUp.click()


    firstElement = browser.find_element_by_xpath("//ul[contains(@class, 'products-list cell-list')]/li[1]/div[@class='item-info']/p[1]/a")
    firstElement.click()


finally:
    sleep(10)
    browser.quit()
