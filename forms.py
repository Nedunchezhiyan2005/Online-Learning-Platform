from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional, URL
from models import User

class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[
        DataRequired(message="Full name is required."),
        Length(min=2, max=100, message="Full name must be between 2 and 100 characters.")
    ])
    email = StringField('Email Address', validators=[
        DataRequired(message="Email address is required."),
        Email(message="Please enter a valid email address."),
        Length(max=120)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password is required."),
        Length(min=6, message="Password must be at least 6 characters long.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message="Please confirm your password."),
        EqualTo('password', message="Passwords must match.")
    ])
    submit = SubmitField('Create Account')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data.lower().strip()).first()
        if user:
            raise ValidationError("This email is already registered. Please sign in or use another email.")


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[
        DataRequired(message="Email address is required."),
        Email(message="Please enter a valid email address.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password is required.")
    ])
    submit = SubmitField('Sign In')


class ProfileUpdateForm(FlaskForm):
    full_name = StringField('Full Name', validators=[
        DataRequired(message="Full name is required."),
        Length(min=2, max=100, message="Full name must be between 2 and 100 characters.")
    ])
    submit = SubmitField('Update Profile')


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[
        DataRequired(message="Current password is required.")
    ])
    new_password = PasswordField('New Password', validators=[
        DataRequired(message="New password is required."),
        Length(min=6, message="New password must be at least 6 characters long.")
    ])
    confirm_new_password = PasswordField('Confirm New Password', validators=[
        DataRequired(message="Please confirm your new password."),
        EqualTo('new_password', message="New passwords must match.")
    ])
    submit = SubmitField('Change Password')


class CourseForm(FlaskForm):
    title = StringField('Course Title', validators=[
        DataRequired(message="Course title is required."),
        Length(max=200)
    ])
    category = SelectField('Category', choices=[
        ('Cloud & DevOps', 'Cloud & DevOps'),
        ('Web Development', 'Web Development'),
        ('Data Science & AI', 'Data Science & AI'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Software Engineering', 'Software Engineering'),
        ('Databases', 'Databases')
    ], validators=[DataRequired(message="Please select a category.")])
    instructor = StringField('Instructor Name', validators=[
        DataRequired(message="Instructor name is required."),
        Length(max=120)
    ])
    duration = StringField('Estimated Duration (e.g. 6 Weeks, 20 Hours)', validators=[
        DataRequired(message="Course duration is required."),
        Length(max=50)
    ])
    description = TextAreaField('Course Overview & Description', validators=[
        DataRequired(message="Description is required.")
    ])
    learning_objectives = TextAreaField('Learning Objectives (one per line)', validators=[
        Optional()
    ])
    is_published = BooleanField('Published and visible to students', default=True)
    submit = SubmitField('Save Course')


class LessonForm(FlaskForm):
    title = StringField('Lesson Title', validators=[
        DataRequired(message="Lesson title is required."),
        Length(max=200)
    ])
    lesson_order = IntegerField('Lesson Order / Sequence Number', default=1, validators=[
        DataRequired(message="Lesson order is required.")
    ])
    content = TextAreaField('Lesson Content / Tutorial Material', validators=[
        DataRequired(message="Lesson content is required.")
    ])
    resource_url = StringField('External Resource / Documentation Link (Optional)', validators=[
        Optional(),
        Length(max=500)
    ])
    submit = SubmitField('Save Lesson')
