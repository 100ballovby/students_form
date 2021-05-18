from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'try-to-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *
from routes import *


if __name__ == '__main__':
    app.run(debug=True)
