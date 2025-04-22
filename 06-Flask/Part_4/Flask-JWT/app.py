from flask import Flask, render_template
from routes.user import user_bp
from flask_jwt_extended import JWTManager  # JWT

app = Flask(__name__)
configure_jwt(app)  # JWT 관련 추가 설정을 적용합니다.

app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)