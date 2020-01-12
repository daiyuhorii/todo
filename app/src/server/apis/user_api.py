from flask_restful  import Resource, reqparse, abort
from flask import jsonify

from server.models import User, UserSchema
from server.database import db

class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', required=True)
        self.reqparse.add_argument('password', required=True)
        super(UserAPI, self).__init__()
    
    def get(self):
        users = db.session.query(User).all()
        if users == None:
            abort(404)
        
        jsondata = UserSchema(many=True).dump(users)
        return jsonify({'items': jsondata})
