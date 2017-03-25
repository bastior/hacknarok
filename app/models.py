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

# idk if it works
# tags = db.Table('tags',
#     db.Column('Offer_id', db.Integer, db.ForeignKey('Offer.id')),
#     db.Column('Technology_id', db.Integer, db.ForeignKey('Technology.id'))
# )


class Technology(db.Model):
    __tablename__ = 'Technology'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Offer(db.Model):
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)
    offer_title = db.Column(db.String(250))
    lower_bound_cash = db.Column(db.Integer)
    higher_bound_cash = db.Column(db.Integer)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'))
    # idk if it works
    # tags = db.relationship('Technology', secondary=tags,
    #    backref=db.backref('Offer', lazy='dynamic'))


class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    offers = db.relationship('Offer', backref='recruiter',
                                lazy='dynamic')


class Recruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass
