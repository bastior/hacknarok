from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    offer_title = db.Column(db.String(250))
    lower_bound_cash = db.Column(db.Integer)
    higher_bound_cash = db.Column(db.Integer)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    pass


class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass


class Recruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass
