from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Regexp


class SignupForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(),
                    Length(min=4, max=20),
                    Regexp(r'^[a-zA-Z0-9]+$', message='No spaces in username!')],
        render_kw={'placeholder': 'Username', 'class': 'form-control'},
    )
    password = PasswordField(
        validators=[InputRequired(),
                    Length(min=4, max=20)],
        render_kw={'placeholder': 'Password', 'class': 'form-control'},
    )
    signup = SubmitField(render_kw={'class': 'btn btn-outline-success'})


class LoginForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(),
                    Length(min=4, max=20)],
        render_kw={'placeholder': 'Username', 'class': 'form-control'}
    )
    password = PasswordField(
        validators=[InputRequired(),
                    Length(min=4, max=20)],
        render_kw={'placeholder': 'Password', 'class': 'form-control'},
    )
    login = SubmitField(render_kw={'class': 'btn btn-outline-success'})


class CafeForm(FlaskForm):
    name = StringField(
        validators=[InputRequired()],
        render_kw={'placeholder': 'name', 'class': 'form-control'}
    )
    address_street = StringField(
        validators=[InputRequired()],
        render_kw={'placeholder': '123 Place Street', 'class': 'form-control'}
    )
    address_state = StringField(
        validators=[InputRequired()],
        render_kw={'placeholder': 'California', 'class': 'form-control'}
    )

    mmmroasty = SubmitField(render_kw={'class': 'btn btn-outline-success'})

class CSRFProtection(FlaskForm):
    """ CSRF protection use only, no fields """