# define task model

# fields:
# _id, writer, content, _limit


from sqlalchemy import CHAR, INTEGER, TEXT
from flask_marshmallow.fields import fields
from server.database import db, ma

class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(INTEGER, primary_key=True)
    user_id = db.Column(CHAR(7), nullable=False)
    content = db.Column(TEXT, nullable=False)
    _limit = db.Column(CHAR(10), nullable=False)

    def __init__(self, user_id, content, _limit):
        self.user_id = user_id
        self.content = content
        self._limit = _limit

    def __repr__(self):
        return "<Task(task_id='%s', user_id='%s', content='%s', _limit='%s')>" % (
            self.task_id,
            self.user_id,
            self.content,
            self._limit
        )

class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task