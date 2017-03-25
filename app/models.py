from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %s>' % self.email

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


# idk if it works
tags = db.Table('tags',
    db.Column('offer_id', db.Integer, db.ForeignKey('offer.id')),
    db.Column('technology_id', db.Integer, db.ForeignKey('technology.id'))
)

class Technology(db.Model):
    __tablename__ = 'technology'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Offer(db.Model):
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)
    offer_title = db.Column(db.String(250))
    lower_bound_cash = db.Column(db.Integer)
    higher_bound_cash = db.Column(db.Integer)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'))
    tags = db.relationship('technology', secondary=tags,
        backref=db.backref('offer', lazy='dynamic'))


class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    offers = db.relationship('Offer', backref='recruiter',
                                lazy='dynamic')


class Recruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
