from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
class UserForm(FlaskForm):
   fname = StringField("First Name")
   lname = StringField("Last Name")
   email = StringField("Email")
   submit = SubmitField("Submit")