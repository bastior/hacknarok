from flask import Flask
from flask import render_template

from db import db
from login import login_manager
from views.logins import login_blueprint
from views.users import user_blueprint
from views.offers import offer_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(user_blueprint)
app.register_blueprint(offer_blueprint)
app.register_blueprint(login_blueprint)
with app.app_context():
    db.create_all()


@app.route("/")
def hello():
    return str(db.metadata.sorted_tables[0].columns)

def create_technology_table():
    db.engine.execute("INSERT INTO technology (name) VALUES ('C++')")
    db.engine.execute("INSERT INTO technology (name) VALUES ('Java')")
    db.engine.execute("INSERT INTO technology (name) VALUES ('C#')")
    db.engine.execute("INSERT INTO technology (name) VALUES ('Python')")
    db.engine.execute("INSERT INTO technology (name) VALUES ('Javascript')")
    db.engine.execute("INSERT INTO technology (name) VALUES ('MongoDB')")
    db.engine.execute("INSERT INTO technology (name) VALUES ('CSS')")
