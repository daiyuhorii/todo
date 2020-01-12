from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
Session = db.session
def init_db(app):
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
