The current aim of this project is to build a program that:
1. listens for alerts/email
1. navigates to the advertisement
1. fills out the initial application forms
1. send the application form.

## Creating a virtual environment
Firstl,y I would like to create a virtual environment for this project.

Here is a link that I have followed to do this: https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b

These are the commands necessary to setup a virtual environment:
$ python --version (Python 3.7.3)
$ pip install virtualenv
$ python -m venv C:\Users\Gerald\Documents\Personal\Coding\Projects\apartment-application-automation/venv
$ venv\scripts\activate
(venv) $ pip install ...
(venv) $ deactivate
$ pip freeze > requirements.txt
$ pip install -r requirements.txt

### Adding venv folder to .gitignore
$ echo venv/ >> .gitignore

## Listening to email account
I want the program to run each time I get an email from the "Daft.ie Enquiry <noreply@daft.ie>" email account. This will be the first feature I work on.

The link I am currently reading specifies that their program reads a set amount of emails from their account when they run their program. I could use this solution and run the program manually whenever I get the notification. This would add some extra labour, but would release the need to constantly have the program running.

Let's try the above approach. (https://www.thepythoncode.com/article/reading-emails-in-python)

I had to use a device specific password to bypass 2-step authentication: https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OfScAjeZuVa9NdZwliKl6so5suPRhRH72dewBEk7PflLBL4RRRIV2KQFXKZ2ZcE_LerGCrREx4mV0_NPplTdFJQvEoOQ

## Form Completions

Using Selenium for this? https://automatetheboringstuff.com/chapter11/#:~:text=Controlling%20the%20Browser%20with%20the%20selenium%20Module
https://www.geeksforgeeks.org/automatically-filling-multiple-responses-into-a-google-form-with-selenium-and-python/

{
    venv\scripts\activate
    pip install selenium
    deactivate
}

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

