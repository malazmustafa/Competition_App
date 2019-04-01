from flask import Flask, render_template, request

app = Flask("MyApp") 

@app.route('/')
def form():
    return render_template('index.html')

@app.route("/signup", methods=["POST"]) 
def sign_up():
    firstname = request.form["firstname"]
    appendFile = open ('form_data.txt','a')
    appendFile.write("\n" + firstname + "\n") #adds new info without deleting previous info
    appendFile.close()

    lastname = request.form["lastname"]
    appendFile = open ('form_data.txt','a')
    appendFile.write(lastname + "\n") #adds new info without deleting previous info
    appendFile.close()


    email = request.form["email"]
    appendFile = open ('form_data.txt','a')
    appendFile.write(email + "\n") #adds new info without deleting previous info
    appendFile.close()
    return "All OK" 

app.run(debug=True)
