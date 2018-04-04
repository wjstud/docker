from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange
from simpledu.models import db, User, Course

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Password again', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username used')
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email used')
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')
    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('email not register')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password error')
    submit = SubmitField('Submit')

class CourseForm(FlaskForm):
    name = StringField('course name', validators=[Required(), Length(5, 32)])
    description = TextAreaField('course desc', validators=[Required(), Length(20, 256)])
    image_url = StringField('封面图片地址', validators=[Required(), URL()])
    author_id = IntegerField('author ID', validators=[Required(), NumberRange(min=1, message='无效的用户ID')])
    submit = SubmitField('submit')

    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('user not exist')

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

class UserForm(FlaskForm):
    username = StringField('username', validators=[Required(), Length(3, 24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    submit = SubmitField('submit')

    def validate_username(self, field):
        if User.query.get(self.username.data):
            raise ValidationError('username used')
    
    def validate_email(self, field):
        if User.query.get(self.email.data):
            raise ValidationError('email used')

    def create_user(self):
        user = User()
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, user):
        self.populate_obj(course)
        db.session.add(user)
        db.session.commit()
        return user

