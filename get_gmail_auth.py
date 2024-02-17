import gmail
import email
from email.header import decode_header
import imaplib 

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
