from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms.validators import DataRequired, ValidationError


class ContactForm(Form):
    name = StringField('Name of student',
                       validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'),
                                           ('F', 'Female'),
                                           ('O', 'Other')])
    address = TextAreaField('Address')
    email = TextAreaField('Email',
                          validators=[DataRequired()])
    age = IntegerField('Age')
    language = SelectField('Languages', choices=[('cpp', 'C++'),
                                                 ('py', 'Python'),
                                                 ('jar', 'Java')])
    submit = SubmitField('Send!')