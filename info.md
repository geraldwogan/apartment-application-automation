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


