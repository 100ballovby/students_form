from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'try-to-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *
from routes import *


if __name__ == '__main__':
    app.run(debug=True)
