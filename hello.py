import requests
from flask import Flask, render_template, request
app = Flask("Competition_App")

def send_simple_message(email, firstname):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org/messages",
        auth=("api", "b5e6c9e56fab046908f1e9273b944409-de7062c6-e7190b95"),
        files= [("attachment", ("test.jpg", open("/Users/anastasiaaniwa/Desktop/CodeFirstGirls/Python/my_app/static/images/test.jpg", "rb").read
        ()))],
        data={"from": "Excited User <postmaster@sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org>",
        "to": [email],
        "subject": "Hello " + firstname,
        "text": "Welcome! ",
        "html": "<html><b>Welcome!</b></html>",
        })



@app.route("/") #@app.route specifies what path to take to find a function
def hello_someone():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    send_simple_message (form_data["email"], form_data["firstname"]) #form_data is a variable to help you store information
    return "All OK"

    app.run(debug=True, port=1235)
