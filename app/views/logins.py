from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask.ext.login import login_user
from flask.views import MethodView

from login import login_manager
from models import User

login_blueprint = Blueprint('login', __name__, template_folder='../templates/logins')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class LoginView(MethodView):
    def get(self):
        return render_template('login_form.html')

    def post(self):
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)
            flash('Logged in')
        return redirect('/')

login_blueprint.add_url_rule('/login', view_func=LoginView.as_view('login'))
