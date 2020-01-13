from flask_restful import Resource, reqparse, abort
from flask import jsonify, request, redirect
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

        # check duplicates later
        user_id = request.form['user_id']
        print("\nreceived user_id: " + user_id)
        password = request.form['password']
        print("received password: " + password)
        # validation
        valid_user = db.session.query(Student).filter(Student.user_id==user_id).one()
        if valid_user is not None:
            print("\n=============\n"+ "DUPLICATE USER\n" + "=============\n")
            return redirect('/signup')
        user = Student(user_id, password)
        session = Session
        session.add(user)
        session.commit()
        return redirect('/')
