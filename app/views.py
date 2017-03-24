from flask import Blueprint
from flask import redirect

from db import db
from models import User

user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route('/add')
def add():
    user = User('xDddd', 'adddd@twojaaa.com')
    db.session.add(user)
    db.session.commit()
    return redirect('/')


