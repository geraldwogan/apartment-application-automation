import json
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# account credentials
json_file = open("secret.json")
variables = json.load(json_file)
json_file.close()

def completeForm(link):

    link= 'https://www.daft.ie/share/9-sarsfield-quay-apartments-liffey-street-west-d-stoneybatter-dublin-7/5587064'

    # Selenium Web Driver specifically for chrome, download from here: https://chromedriver.chromium.org/downloads
    service = webdriver.ChromeService('chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Open webpage
    # driver = webdriver.Chrome()
    driver.get(link)

    # Wait for page to load
    time.sleep(.5)

    # Accept the cookie settings
    # e = driver.find_element(By.XPATH, '//button[contains(., "ACCEPT ALL"]')
    e = driver.find_elements(By.XPATH, '//button')
    e[1].click()

    time.sleep(1)

#   Sign-in to bypass captcha
    e = driver.find_element(By.XPATH, '//a[contains(., "Sign in")]')
    e.click()

    time.sleep(.5)

    f = driver.find_elements(By.XPATH, '//input')
    time.sleep(.5)
    f[0].send_keys(variables["email"])
    f[1].send_keys(variables["daft_pass"])
    time.sleep(.5)
    # e = driver.find_element(By.XPATH, '//input[contains(., "SIGN IN")]')
    e = driver.find_element(By.CLASS_NAME, 'login__button')

    e.click()
    time.sleep(.5)

    # Click the Email Agent Button
    e = driver.find_element(By.XPATH, '//button[contains(., "Email")]')
    e.click()

    time.sleep(4)

    # Fill-out Form 
    f = driver.find_elements(By.XPATH, "//*[contains(@id,'keyword')]")

    f[0].send_keys(variables["first_name"])
    f[1].send_keys(variables["last_name"])
    f[2].send_keys(variables["email"])
    f[3].send_keys(variables["phone_number"])

    # Multiline text entry require (SHIFT + ENTER) for a newline.
    t = driver.find_elements(By.XPATH, '//textarea')
    for part in variables["pitch"].split('\n'):
        t[1].send_keys(part)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        
    time.sleep(10)

    # Send form
    # e = driver.find_element(By.XPATH, '//button[contains(., "Send")]')
    # e.click()

    return

completeForm('b')