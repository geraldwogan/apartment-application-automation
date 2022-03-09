import imaplib 
import email
from email.header import decode_header
import webbrowser
import os
import json
import re

# account credentials
json_file = open("apartment-application-automation/secret.json")
variables = json.load(json_file)
json_file.close()
password = variables["device_pass"]
username = variables["username"]


# We need the clean() function later to create folders without spaces and special characters.
def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text) 


# # create an IMAP4 class with SSL (connect to the IMAP server)
# imap = imaplib.IMAP4_SSL("imap.gmail.com")
# # authenticate
# imap.login(username, device_pass)


imap = imaplib.IMAP4_SSL("imap.gmail.com",993)
imap.login(username, password)
# M.starttls() #Run it once and once you get error then remove it and recompile and you will be connected
# M.select()
# typ, data = M.search(None, 'ALL')
# for num in data[0].split():
#     typ, data = M.fetch(num, '(RFC822)')
#     print('Message %s\n%s\n' % (num, data[0][1]))
# M.close()

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
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:", subject)
            print("From:", From)     

            if From == '"Daft.ie Property Alert" <noreply@daft.ie>':# & From == 'Daft.ie':
                # if the email message is multipart
                if msg.is_multipart():
                    print('Message is multipart')
                    # iterate over email parts
                    for part in msg.walk():
                        print('---Part START---')
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
                                # Find link using regex
                                links = re.findall('\((.*?)\)', body)
                                print(links)
                                webbrowser.open(links[0])

                            print(body)

                        # elif "attachment" in content_disposition:
                        #     # download attachment
                        #     filename = part.get_filename()
                        #     if filename:
                        #         folder_name = clean(subject)
                        #         if not os.path.isdir(folder_name):
                        #             # make a folder for this email (named after the subject)
                        #             os.mkdir(folder_name)
                        #         filepath = os.path.join(folder_name, filename)
                        #         # download attachment and save it
                        #         open(filepath, "wb").write(part.get_payload(decode=True))
                        print('---Part End---')
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)
                # if content_type == "text/html":
                #     # if it's HTML, create a new HTML file and open it in browser
                #     folder_name = clean(subject)
                #     if not os.path.isdir(folder_name):
                #         # make a folder for this email (named after the subject)
                #         os.mkdir(folder_name)
                #     filename = "index.html"
                #     filepath = os.path.join(folder_name, filename)
                #     # write the file
                #     open(filepath, "w").write(body)
                #     # open in the default browser
                #     webbrowser.open(filepath)
                print("="*100)
# close the connection and logout
imap.close()
imap.logout()

