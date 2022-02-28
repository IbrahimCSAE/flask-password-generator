
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        
        password_conditions = [int(x) for x in request.form.getlist('mycheckbox')]
        length = int(request.form.get('length'))
        print(length)
        print(password_conditions)
        all = ""
        password = ""
        if 1 in password_conditions:
            all += string.punctuation
        else:
            all = all
        if 2 in password_conditions:
            all += string.digits
        else:
            all = all
        if 3 in password_conditions:
            all += string.ascii_lowercase
        else:
            all = all
        if 4 in password_conditions:
            all +=string.ascii_uppercase
        else:
            all = all
        if all == "":
            all = string.punctuation + string.digits + string.ascii_lowercase + string.ascii_uppercase
        password = "".join(random.sample(all, length))
        
    return render_template("index.html",password = password)


if __name__ == "__main__":
    app.run(debug=True)