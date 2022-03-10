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


# account credentials
json_file = open("apartment-application-automation/secret.json")
variables = json.load(json_file)
json_file.close()
password = variables["device_pass"]
username = variables["username"]

def getPropertyLink():

    # Login to Gmail account using secrets.json variables
    imap = imaplib.IMAP4_SSL("imap.gmail.com",993)
    imap.login(username, password)

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




def formCompletion(link):


    link= 'https://www.daft.ie/for-rent/apartment-whitworth-road-drumcondra-dublin-3/3723347'
    # wait for one second, until page gets fully loaded

    data = ['Gerald Wogan', 'geraldwogan@gmail.com', '0879999999', 'Test message']


    driver =  webdriver.Chrome('apartment-application-automation\chromedriver.exe')
    time.sleep(5)

    # Open webpage
    # webbrowser.open(link)

    driver.get(link)
    time.sleep(5)
    e = driver.find_elements(By.XPATH, '//button')
    # e = driver.find_element(By.XPATH, '//button[contains(., "Accept All"]')
    e[1].click()

    time.sleep(5)

    e = driver.find_element(By.XPATH, '//button[contains(., "Email Agent")]')
    print(e)
    e.click()

    time.sleep(2)


    e = driver.find_element(By.XPATH, '//button[contains(., "Send")]')
    print(e)
    e.click()


    e = driver.find_element(By.XPATH, '//button[contains(., "Send")]')


    # Use Selenium to fill out web form

    # 1. Open webpage

    # 1. Click 'Email' button
    # 1. Fill-out form
    #     1. Full Name
    #     1. Your email
    #     1. Your phone number (Optional)
    #     1. Message
    #     1. Click 'Send' button
    # 1. Close webpage
    # 1. Wait for 5 minutes (?)
    # 1. Check email for make sure we have a new Daft Enquiry for the property.


formCompletion('b')

