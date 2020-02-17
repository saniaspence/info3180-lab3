from flask_wtf import FlaskForm
from wtforms import Form,StringField, SubmitField, TextAreaField,TextField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired("Please enter your name."), Length(min=2, max=20)])
    
    email = StringField('Email',
                        validators=[DataRequired("Please enter your email address."),Email()])
    
    subject = StringField('Subject',
                          validators=[DataRequired("Please enter a subject."), Length(min=2, max=200)])
    
    message = TextAreaField('Message',
                          validators=[DataRequired("Please enter a message."), Length(min=2, max=10000)])

    submit = SubmitField('Send')
