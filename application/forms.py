from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.models import Account_details

class LoginForm(FlaskForm):
    login = StringField("login",
        validators=[
                DataRequired()
            ]
        )

    password = PasswordField("password",
        validators=[
                DataRequired()
            ]
        )

    remember = BooleanField("Remember me")
    submit = SubmitField("Login")



class RegistrationForm(FlaskForm):
    login = StringField("login",
        validators=[
                DataRequired()
            ]
        )

    password = PasswordField("password",
        validators=[
                DataRequired()
            ]
        )

    confirm_password = PasswordField("Confirm Password",
        validators=[
                DataRequired(),
                EqualTo("password")
            ]
        )

    submit = SubmitField("Sign up")
    
    def validate_login(self, login):
        user = Account_details.query.filter_by(login = login.data).first()

        if user:
            raise ValidationError("Login already in database.")


class PostForm(FlaskForm):
    first_name = StringField("First Name",
        validators = [
            DataRequired(),
            Length(min=1, max=64)
        ]
    )
    last_name = StringField("Last Name",
        validators = [
            DataRequired(),
            Length(min=1, max=64)
        ]
    )
    title = StringField("Title",
        validators = [
            DataRequired(),
            Length(min=1, max=100)
        ]
    )
    content = StringField("Content",
        validators = [
            DataRequired(),
            Length(min=1, max=100)
        ]
    )

    submit = SubmitField("Post Content")

