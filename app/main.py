from flask import Flask
from flask import render_template

from db import db
from views import user_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
app.register_blueprint(user_blueprint)
with app.app_context():
    db.create_all()


@app.route("/")
def hello():
    return render_template('index.html')


