from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'try-to-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        return render_template('success.html')
    else:
        return render_template('contacts.html', form=form)


if __name__ == '__main__':
    app.run()
