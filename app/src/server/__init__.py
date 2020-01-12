from flask import Flask, Response, request, render_template, redirect
from flask_restful import Api
from .database import init_db, db
from . import hoge
from .apis import *
from flask_login import LoginManager, login_required, logout_user
from hashlib import sha256
from .login import Auth


def create_app():
    # create flask app, enable it to read a relatvie path to config.
    app = Flask(__name__,
                instance_relative_config=True,
                template_folder='./templates',
                static_url_path='/js')
    app.config.from_object('server.config.default.Config')
    # initializes MySQL database and login auth.
    app.secret_key = sha256("teamnull".encode('utf-8')).digest()
    init_db(app)

    login_manager = LoginManager(app)
    @login_manager.user_loader
    def load_user(user_id):
        load_user = db.session.query(Student)\
                    .filter(Student.user_id == user_id).first()
        return load_user

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            return render_template('login.html')
    
    @app.route('/signup')
    def signup():
        return render_template('signup.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect('/login')

    @app.route('/home')
    @login_required
    def protected():
        return render_template('home.html')

    # create an Api object and append WebAPI resource URIs.
    api = Api(app)

    api.add_resource(UserAPI, '/users')
    api.add_resource(Student_API, '/students')
    api.add_resource(Auth, '/auth')
    api.add_resource(TaskAPI, '/task')

    # delete this when apis are made
    blueprints = [hoge]
    for blueprint in blueprints:
        app.register_blueprint(blueprint.app)

    return app


app = create_app()
