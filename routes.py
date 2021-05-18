from flask import request, render_template, redirect
from forms import ContactForm
from app import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        return render_template('success.html')
    else:
        return render_template('contacts.html', form=form)