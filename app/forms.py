from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class UploadForm(FlaskForm):
    file = FileField('Upload an Image', validators=[
        FileRequired(), 
        FileAllowed(['jpg', 'png'], 'Just Images!')
    ])
    submit = SubmitField('Upload')