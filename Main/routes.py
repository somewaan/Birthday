from Main import app
from flask import render_template, redirect, url_for, request


@app.route('/')
def home():
    return redirect(url_for('birthday_page'))


@app.route('/submit', methods=["GET", "POST"])
def birthday_page():
    if request.method == "POST":
        user = request.form["name"]
        # name1 = ["bhavana", "Bhavana", "sandrala", "Sandrala", "Bhavana sandrala", "bhavana sandrala", "Sandrala bhavana", "Sandrala Bhavana",
        #          "Baanaa"]
        name1 = ["bhavana", "bhavana sandrala", "Bhavana", "sandrala", "Sandrala", "Bhavana sandrala",
                 "bhavana sandrala", "Sandrala bhavana", "Sandrala Bhavana",
                 "Pinni", "Eddy", "Baanaa", "Thingari", "Potti", "Mental", "Darling",
                 "Chiflada", "Kukka pilla", "Kothi", "Buji kana", "Bujji", "Bhanu",
                 "Ammulu", "Bhavanalii", "Bhavanalli", "Ammu", "Bhavs", "Bangaaram"]
        while name1:
            if user in name1:
                return redirect(url_for("displaying_name", name=user))
            else:
                return f'<h1>Sorry {user}! You will get your wishes on your birthday</h1>'
    return render_template('submit.html')


@app.route('/<name>')
def displaying_name(name):
    return render_template('birthday.html', name=name)
