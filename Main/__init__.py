from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '3c3db508917702c31055e737'

from Main import routes