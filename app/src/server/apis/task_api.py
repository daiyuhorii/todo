from flask_restful  import Resource, reqparse, abort
from flask import jsonify, request, session, Response
from server.models import Task, TaskSchema
from server.database import db, Session
import json

class TaskAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('user_id', required=True)
        self.reqparse.add_argument('content', required=True)
        self.reqparse.add_argument('_limit', required=True)

        super(TaskAPI, self).__init__()
    
    def get(self):
        tasks = db.session.query(Task).all()
        if tasks == None:
            return "No tasks"
        
        jsondata = TaskSchema(many=True).dump(tasks)
        return jsonify({'items': jsondata})
    
    def post(self):
        if request.headers['Content-Type'] != 'application/json':
            return jsonify({'error': 'not a json type'}), 400
        
        req = request.get_json()
        print("\n============\n", req, "\n============\n")
        user_id = req['user_id']
        content = req['content']
        limit = req['_limit']
        task = Task(user_id, content, limit)
        sess = Session
        sess.add(task)
        sess.commit()
        
        result = db.session.query(Task).filter(Task.user_id == user_id).all()
        result = TaskSchema(many=True).dump(result)
        result = result[-1]
        print("POST: " + json.dumps(result))
        data = jsonify({'items': result})
        return data
    
    def delete(self):
        if request.headers['Content-Type'] != 'application/json':
            return jsonify({'error': 'not a json type'}), 400
        
        req = request.get_json()
        print("\n============data============\n", req, "\n============================\n")
        task_id = req['task_id']
        task_id = int(task_id)
        
        db.session.query(Task).filter(Task.task_id == task_id).delete()
        db.session.commit()
        result = db.session.query(Task).filter(Task.task_id == task_id-1).all()
        result = TaskSchema(many=True).dump(result)
        data = jsonify({'items': result})
        return data