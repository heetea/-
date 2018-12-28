from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/heetae/desktop/chromedriver/chromedriver')

driver.get('https://beergameapp.firebaseapp.com/')

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("//*[@id='site-wrapper']/div[2]/div/div/div[2]/button[1]").click()

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/form[1]/div[2]/a").click()

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("//*[@id='gameName']")

from random import *
 
i = randint(1, 100) 

elem.send_keys(10000*i)

elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/form[2]/div[2]/button").click()

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/a").click()

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("//*[@id='site-wrapper']/div[2]/div/div/section/div[2]/div/ul/li[1]/a/h3").click()

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("//*[@id='retailer']/div[2]/div/div[2]/div[1]/div[2]/div[2]/button").click()

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/label/input").click()

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/button").click()


driver.implicitly_wait(5)

btn = 0
while btn < 40 :
   
    elem = driver.find_element_by_xpath("//*[@id='retailer']/div[2]/div/div[2]/div[1]/div[2]/div[2]/button").click()
    driver.implicitly_wait(5)
    btn += 1
