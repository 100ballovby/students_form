from flask import request, render_template, redirect
from forms import ContactForm
from app import app, db
from models import Contact


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        new_contact = Contact(
            name=form.name.data.lower().title(),
            gender=form.gender.data,
            address=form.address.data,
            email=form.email.data.lower().strip(),
            age=form.age.data,
            language=form.language.data
        )
        db.session.add(new_contact)  # добавление
        db.session.commit()  # применение
        return render_template('success.html')
    else:
        return render_template('contacts.html', form=form)