from flask import Flask , request
import test

app = Flask(__name__)

@app.route('/')
def home():
    return "Helo, This is Main Page"

@app.route('/about')
def about():
    return "This is about Page"

@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    request.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)
    
    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("POST")

    return "success"


if __name__ == "__main__":
    print("__name__ : ", __name__)
    app.run(debug=True)