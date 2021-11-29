from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class UserForm(FlaskForm):
   fname = StringField("First Name", [validators.DataRequired(), validators.Length(min=3, max=100)])
   lname = StringField("Last Name", [validators.DataRequired(), validators.Length(min=3, max=100)])
   email = StringField("Email", [validators.DataRequired(), validators.Email("Please provide a valid email address.")])
   submit = SubmitField("Submit")

class User:
   # def __init__(self) -> None:
   #     self.
       pass