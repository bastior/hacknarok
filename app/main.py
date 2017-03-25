from flask import Flask
from flask import render_template

from db import db
from views.users import user_blueprint
from views.offers import offer_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
app.register_blueprint(user_blueprint)
app.register_blueprint(offer_blueprint)
with app.app_context():
    db.create_all()


@app.route("/")
def hello():
    return str(db.metadata.sorted_tables[1].columns)


