The current aim of this project is to build a program that:
1. listens for alerts/email
1. navigates to the advertisement
1. fills out the initial application form
1. sends the application form

## Listening to email account
I want the program to run each time I get an email from the "Daft.ie Enquiry <noreply@daft.ie>" email account.

The guide I am currently reading specifies that their program reads a set amount of emails from their account when they run their program. I could use this solution and run the program manually whenever I get the notification. This would add some extra labour, but would release the need to constantly have the program running.

Let's try the above approach. (https://www.thepythoncode.com/article/reading-emails-in-python)

I had to use a device specific password to bypass 2-step authentication: https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OfScAjeZuVa9NdZwliKl6so5suPRhRH72dewBEk7PflLBL4RRRIV2KQFXKZ2ZcE_LerGCrREx4mV0_NPplTdFJQvEoOQ

I did the original work with imaplib, but it looks like it could be done with a Gmail API too: https://www.thepythoncode.com/article/use-gmail-api-in-python

## Form Completions
Using Selenium for this? https://automatetheboringstuff.com/chapter11/#:~:text=Controlling%20the%20Browser%20with%20the%20selenium%20Module
https://www.geeksforgeeks.org/automatically-filling-multiple-responses-into-a-google-form-with-selenium-and-python/
https://selenium-python.readthedocs.io/locating-elements.html

Installed the chrome driver for Selenium to work with chrome: https://chromedriver.storage.googleapis.com/index.html?path=99.0.4844.51/
1. Open webpage
1. Click 'Email' button
1. Fill-out form
    1. Full Name
    1. Your email
    1. Your phone number (Optional)
    1. Message
    1. Click 'Send' button
1. Close webpage
1. Wait for 5 minutes (?)
1. Check email for make sure we have a new Daft Enquiry for the property.

## Run this program.py
C:\Users\Gerald\Documents\Personal\Coding\Projects\apartment-application-automation\venv\Scripts\python.exe program.py
