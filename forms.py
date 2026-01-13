from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username: StringField = StringField(validators=[InputRequired()])
    password: PasswordField = PasswordField(validators=[InputRequired()])
    submit: SubmitField = SubmitField("Login")

class RegisterForm(FlaskForm):
    username: StringField = StringField(validators=[InputRequired(), Length(min=3)])
    password: PasswordField = PasswordField(validators=[InputRequired(), Length(min=5)])
    submit: SubmitField = SubmitField("Register")

class ChallengeForm(FlaskForm):
    flag: StringField = StringField(validators=[InputRequired()])
    submit: SubmitField = SubmitField("Submit Flag")

class AdminChallengeForm(FlaskForm):
    title: StringField = StringField(validators=[InputRequired()])
    description: TextAreaField = TextAreaField(validators=[InputRequired()])
    flag: StringField= StringField(validators=[InputRequired()])
    points: IntegerField = IntegerField(validators=[InputRequired()])
    submit: SubmitField = SubmitField("Create")

class ChangePasswordForm(FlaskForm):
    old_password: PasswordField = PasswordField("Oud wachtwoord", validators=[InputRequired()])
    new_password: PasswordField = PasswordField("Nieuw wachtwoord", validators=[InputRequired(), Length(min=5)])
    submit: SubmitField = SubmitField("Wijzig wachtwoord")

class ProfilePicForm(FlaskForm):
    picture: FileField = FileField("Upload profielfoto", validators=[FileAllowed(["jpg", "png", "jpeg"], "Alleen afbeeldingen!")])
    submit: SubmitField = SubmitField("Wijzig profielfoto")