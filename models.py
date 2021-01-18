from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    users_all = db.Column(JSON)
    users_no_stop_words = db.Column(JSON)

    def __init__(self, url, users_all, users_no_stop_words):
        self.url = url
        self.users_all = users_all
        self.users_no_stop_words = users_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
