from flask import Flask, render_template, request

#app = Flask(__name__)

#@app.route('/', methods=['GET', 'POST'])
#def form():
    #return render_template('index.html')

#@app.route('/hello', methods=['GET', 'POST'])
#def hello():
#    return render_template('greeting.html', say=request.form['say'], to=request.form['to'])

#if __name__ == "__main__":
 #   app.run()
#text= 'blah blah blah'
#saveFile = open ('form_data.txt','w')
#saveFile.write(text) #writing to a file but it clears it
#saveFile.close() 

#apendMe = '\n This is new information'
#appendFile = open ('form_data.txt','a')
#appendFile.write(appendMe) #adds new info without deleting previous info
##appendFile.close()

#reading from a file
#readMe = open('form_data.txt','r').readlines()  #reading from an excel sheet
#print(readMe)
app=Flask("MyApp")


@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "Thanks"


app.run(debug=True)