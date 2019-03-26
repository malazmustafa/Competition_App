import requests
import os
from flask import Flask, render_template, request
from main.hello import send_simple_message
app = Flask("Competition_App")

@app.route("/") #@app.route specifies what path to take to find a function
def hello_someone():
    return render_template("index.html")

@app.route("/index", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    send_simple_message (form_data["email"], form_data["firstname"]) #form_data is a variable to help you store information
    return "All OK"


port = int(os.environ.get('PORT', 2345))
app.run(debug=True, port=port)
