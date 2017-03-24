from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.views import View, MethodView

from db import db
from models import User

user_blueprint = Blueprint('user', __name__, template_folder='templates/users')


@user_blueprint.route('/add')
def add():
    user = User('xDddd', 'adddd@twojaaa.com')
    db.session.add(user)
    db.session.commit()
    return redirect('/')


class ShowUsers(View):
    def get_template_name(self):
        return 'show.html'

    def get_objects(self):
        return User.query.all()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

user_blueprint.add_url_rule('/users/show', view_func=ShowUsers.as_view('show_users'))


class AddUser(MethodView):
    def get_template_name(self):
        return 'add.html'

    def get(self):
        return render_template(self.get_template_name())

    def post(self):
        user = User(request.form['email'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.show_users'))

user_blueprint.add_url_rule('/users/add', view_func=AddUser.as_view('add_user'))
