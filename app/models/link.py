import string
from datetime import datetime
from random import choices

from app.extensions.database import db

class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512))
    slug = db.Column(db.String(5), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.slug = self.generate_slug()

    def generate_slug(self):
        """Generate a random 5 characters slug"""
        chars = string.digits + string.ascii_letters
        slug = ''.join(choices(chars, k=5))

        link = self.query.filter_by(slug=slug).first()

        if link:
            return self.generate_slug()

        return slug
