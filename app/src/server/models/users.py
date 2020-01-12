# define two user types(admin, student) on models/users.py.
# all codes are widely shared on github <github.com/daiyuhorii>,
# so you can reuse these codes or use them as a reference of
# typical flask applications.
# credits to: Daiyu Horii <daiyuhorii@gmail.com>

from server.database import db, ma
from sqlalchemy import CHAR, VARCHAR, INTEGER, TEXT, BOOLEAN
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# define User model and schema
class Student(db.Model, UserMixin):
    __tablename__ = "students"

    # define attributes
    # IDs must be like "xxFIxxx" which consists of seven letters.
    user_id = db.Column(CHAR(7), nullable=False, primary_key=True)
    password = db.Column(VARCHAR(255), nullable=False)
    report_count = db.Column(INTEGER)
    is_allowed_to_add_schedule = db.Column(BOOLEAN, nullable=False)
    msg_from_admin = db.Column(TEXT, nullable=True)

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = generate_password_hash(password)
        self.report_count = 0
        self.is_allowed_to_add_schedule = True
        self.msg_from_admin = ""

    def verify_password(self, password):
        if check_password_hash(self.password, password):
            return True
        else:
            return False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def get(self):
        return self

    @classmethod
    def auth(cls, user_id, password):
        user = db.session.query(Student)\
               .filter(Student.user_id == user_id).first()
        if user.user_id == user_id and\
           check_password_hash(user.password, password):
            return True
        else:
            return False

    def __repr__(self):
        return "<user_id=%s, password=%s, report_count=%s, \
            is_allowed_to_add_schedule=%s>"\
            % (
                self.user_id,
                self.password,
                self.report_count,
                self.is_allowed_to_add_schedule
            )


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student


# define Admin model and schema
class Admin(db.Model):
    __tablename__ = "admin"

    # define  attributes of admin
    # id must be "admin" and others will be failed at validation.
    id = db.Column(CHAR(5), nullable=False, primary_key=True)
    password = db.Column(VARCHAR(255), nullable=False)

    # do not allow admin to change its username
    def __init__(password, self):
        self.password = password

    def __repr(self):
        return "This is an Administrative account. 403 unauthorized."


class AdminSchema(ma.ModelSchema):
    class Meta:
        model = Admin
