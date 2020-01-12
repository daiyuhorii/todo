from sqlalchemy import VARCHAR, CHAR
from flask_marshmallow.fields import fields
from server.database import db, ma

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(CHAR(7), primary_key=True)
    password = db.Column(VARCHAR(255), nullable=False)
    
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def __repr__(self):
        return "<User(id='%s', password='%s')>" % (
            self.id,
            self.password
        )

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    