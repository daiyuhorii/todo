from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from sqlalchemy import VARCHAR, CHAR
from flask_marshmallow.fields import fields
db = SQLAlchemy()
ma = Marshmallow()

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




SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
        **{
            'user': 'root',
            'password': 'teamnull',
            'host': '127.0.0.1:3306',
            'database': 'db2019'
        }
    )
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
@app.route('/')
def connectdb():
    db = SQLAlchemy(app)
    db.session.add(User('17fi088', 'hogehoge'))
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
