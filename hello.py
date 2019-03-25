import requests
from flask import Flask, render_template, request
app = Flask("MyApp")

def send_simple_message(email, username):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org/messages",
        auth=("api", "b5e6c9e56fab046908f1e9273b944409-de7062c6-e7190b95"),
        files= [("attachment", ("test.jpg", open("/Users/anastasiaaniwa/Desktop/CodeFirstGirls/Python/my_app/static/images/test.jpg", "rb").read
        ()))],
        data={"from": "Excited User <postmaster@sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org>",
        "to": [email],
        "subject": "Hello " + username,
        "text": "Hehe look i learnt how to add HTML and attachments to emails! ",
        "html": "<html> Hehe look i learnt how to add <b>HTML</b> and <i>attachments</i> to emails!</html>",
        "o:deliverytime": "Sun, 17 Mar 2019 16:12:00 -0000"})
