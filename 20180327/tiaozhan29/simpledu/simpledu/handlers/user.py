from flask import Blueprint, render_template
from simpledu.models import User, Course

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    users = User.query.all()
    courses = Course.query.all()
    return render_template('user.html', users=users, courses=courses, username=username)
