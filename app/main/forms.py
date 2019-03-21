import re

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, ValidationError, Length, Optional

from app.models import User, Status


def get_users():
    return User.query


def get_status():
    return Status.query


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    name = StringField('User name *', validators=[DataRequired()])
    email = StringField('Email *', validators=[DataRequired()])
    phone = StringField('Phone')

    submit = SubmitField('Submit')


class TaskForm(FlaskForm):
    title = StringField('Title *', validators=[DataRequired()])
    description = TextAreaField('Description')
    due_date = DateField('Due date (format: YYYY-MM-DD)', validators=[Optional()])
    status = QuerySelectField('Task status *', query_factory=get_status, validators=[DataRequired()])
    user = QuerySelectField('Assigned user', query_factory=get_users)

    submit = SubmitField('Submit')

    def validate_due_date(self, due_date):
        if due_date.data:
            print(due_date)
            print(str(due_date.data))
            res = re.findall('(\d{4})-(\d{2})-(\d{2})', str(due_date.data))
            if not res:
                raise ValidationError('Please insert a date with the following format: YY-MM-DD.')


class ModifyDataForm(FlaskForm):
    submit = SubmitField('Modify')