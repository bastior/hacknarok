from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from install import db_install, app_install
from install import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route("/")
def hello():
    db_install.create_all()
    return str(db_install.metadata.sorted_tables[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
    #for t in metadata.sorted_tables:
     #   print(t.name)

