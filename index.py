from flask import Flask, render_template, request

app = Flask("MyApp") 

@app.route('/')
def form():
    return render_template('main.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/html-course')
def htmlcourse():
    return render_template('html-course.html')

@app.route('/python-course')
def pythoncourse():
    return render_template('python-course.html')

@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')

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
    def send_complex_message():
        return requests.post(
        "https://api.mailgun.net/v3/sandbox090dbaf5242b45fc874d57e41d45178f.mailgun.org/messages",
        auth=("api", "25688de742c8818c5bcfaee068327612-de7062c6-d093c5ab"),
        files=[("attachment", ("mummy.jpg", open("Desktop/test.jpg","rb").read()))],
        data={"from": "Excited User <mailgun@sandbox090dbaf5242b45fc874d57e41d45178f.mailgun.org>",
              "to": "email",
              "subject": "Hello",
              "text": "Thank you for siging up."})
    return render_template('courses.html')


app.run(debug=True)

