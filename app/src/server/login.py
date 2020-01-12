from flask_restful import Resource, reqparse
from flask_login import login_user, current_user
from flask import request, redirect, Response, render_template, session
from server.database import db
from server.models import Student
from werkzeug.security import check_password_hash


class Auth(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('user_id', required=True)
        self.parser.add_argument('password', required=True)
        super(Auth, self).__init__()

    def get(self):
        return redirect('/login')

    def post(self):
        self.parser.parse_args()
        self.parser.add_argument('user_id', required=True)
        self.parser.add_argument('password', required=True)

        req_user_id = request.form['user_id']
        req_password = request.form['password']
        print("\n=======\ncurrent user:", current_user, "\n=======\n")

        # validation
        query = db.session.query(Student).filter(Student.user_id == req_user_id).first()
        print(type(query), "\n", query.user_id, query.password)
        if query.user_id == req_user_id and\
           check_password_hash(query.password, req_password):
           session['user_id'] = req_user_id
           login_user(query, remember=True)
           print("\n=======\ncurrent user:", current_user, "\n=======\n")
           return redirect('/home')
        else:
            return redirect('/login')
