# base python image for custom image
FROM python:3.10.11-slim-buster

# create working directory and install pip dependencies
WORKDIR /workdir
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy python project files from local to /hello-py image working directory
COPY . .
COPY ./chromedriver.exe ../

# run the flask server  
CMD [ "python", "-m" , "uvicorn",  "app:app", "--host", "0.0.0.0"]