import imaplib 
import email
from email.header import decode_header
import webbrowser
import os
import json
import re
from selenium import webdriver
# from selenium import WebElement
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# account credentials
json_file = open("secret.json")
variables = json.load(json_file)
json_file.close()

def getPropertyLink():

    # Login to Gmail account using secrets.json variables
    imap = imaplib.IMAP4_SSL("imap.gmail.com",993)
    imap.login(variables["email"], variables["device_pass"])

    # Select folder to read from
    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 2
    # total number of emails
    messages = int(messages[0])

    for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])

                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                print("Subject:", subject)

                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("From:", From)     

                # Only proceed if it is a Property Alert from Daft.ie
                if From == '"Daft.ie Property Alert" <noreply@daft.ie>':# & From == 'Daft.ie':
                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                if('View Property' in body):
                                    # Find link using regex. The first link in the email will be for the property.
                                    links = re.findall('\((.*?)\)', body)

                                    # Open link in web browser
                                    # webbrowser.open(links[0])

                    print("="*100)

    # close the connection and logout
    imap.close()
    imap.logout()

    return links[0]

def completeForm(link):

    link= 'https://www.daft.ie/for-rent/apartment-bronze-en-suite-2022-23-tenancy-41-weeks-brickworks-brickfield-lane-dublin-8/2863979'

    # Selenium Web Driver specifically for chrome, download from here: https://chromedriver.chromium.org/downloads
    driver =  webdriver.Chrome('chromedriver.exe')

    # Open webpage
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
    e = driver.find_element(By.XPATH, '//button[contains(., "Email Agent")]')
    e.click()

    time.sleep(2)

    # Fill-out Form 
    f = driver.find_elements(By.XPATH, '//input')
    f[1].send_keys(variables["first_last"])
    f[2].send_keys(variables["email"])
    f[3].send_keys(variables["phone_no"])
    t = driver.find_elements(By.XPATH, '//textarea')
    t[0].send_keys(variables["pitch"])

    time.sleep(5)

    # Send form
    # e = driver.find_element(By.XPATH, '//button[contains(., "Send")]')
    # e.click()

    return

completeForm('b')