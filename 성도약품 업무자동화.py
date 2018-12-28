from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/heetae/desktop/chromedriver/chromedriver')

driver.get('http://www.pharmon.co.kr/?c=information')

driver.implicitly_wait(5)

elem = driver.find_element_by_name("name") 
elem.send_keys("캅셀")
elem.submit()


driver.implicitly_wait(5)

medisonName = driver.find_element_by_id('rji02').text 

driver.close()

results = []
results.append(medisonName)

import pandas as pd

dataframe = pd.DataFrame(results)

dataframe.to_csv("/Users/heetae/desktop/chromedriver/abx.csv", header=False, index =False)