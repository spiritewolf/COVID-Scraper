from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox(executable_path='/Users/k80/Dev/geckodriver') #replace with your path

userInput = input('Which city do you want to search covid cases? ');

driver.get("https://google.com")

search = driver.find_element_by_name('q')

search.send_keys('covid cases ' + userInput)
search.send_keys(Keys.RETURN)
try:
    results = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'JZLOZd')))
    print('There were ' + results.text + ' new COVID-19 cases reported in' + userInput + ' yesterday.')
except:
    driver.quit()

driver.quit();
