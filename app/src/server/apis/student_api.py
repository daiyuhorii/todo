from flask_restful import Resource, reqparse, abort
from flask import jsonify, request
from server.models import Student, StudentSchema
from server.database import db, Session


# define API associated with Student table.
class Student_API(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('user_id', required=True)
        self.parser.add_argument('password', required=True)
        super(Student_API, self).__init__()

    def get(self):
        sess = db.session.query(Student).all()
        if sess is None:
            return abort(400)
        else:
            data = StudentSchema(many=True).dump(sess)
            return jsonify(data)

    def post(self):
        self.parser.parse_args()
        self.parser.add_argument('user_id', required=True)
        self.parser.add_argument('password', required=True)

        # if content-type is not json, return 400
        if request.headers['Content-Type'] != 'application/json':
            return jsonify(res='error'), 400
        # check duplicates later
        req = request.get_json()
        user_id = req['user_id']
        print("received " + user_id)
        password = req['password']
        print("received " + password)
        user = Student(user_id, password)
        session = Session
        session.add(user)
        session.commit()
        return req
