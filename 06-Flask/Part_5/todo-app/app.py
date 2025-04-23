from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from db import db
from flask_migrate import Migrate


app = Flask(__name__)

# 데이터베이스 및 JWT 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' # local db => 파일 형태의 간단한 데이터 베이스
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['API_TITLE'] = 'Todo API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'

# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

# 모델 및 리소스 불러오기 (이후에 정의)
from models import User, Todo
from routes.auth import auth_blp
from routes.todo import todo_blp

# 간단한 실험 라우터
from flask import request, jsonify, render_template
from werkzeug.security import generate_password_hash

@app.route('/login-page')
def login_page():
    return render_template('login.html')

@app.route('/todos')
def todos_page():
    return render_template('todos.html')

@app.route('/register-page')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "아이디와 비밀번호를 입력하세요"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "이미 존재하는 사용자입니다"}), 409

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "회원가입 성공!"}), 201


# API에 Blueprint 등록
api.register_blueprint(auth_blp)
api.register_blueprint(todo_blp)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
