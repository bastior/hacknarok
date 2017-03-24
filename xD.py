from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route("/")
def hello():
    #return "Hello World from Flask in a uWSGI Nginx Docker container with \
    # Python 3.5 (default)"
    user = {
            'nickname': 'xD'
    }
    return render_template('index.html', user=user, title='home')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
