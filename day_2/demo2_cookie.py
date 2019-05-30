from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    user_id = request.cookies.get('user_id')
    user_name = request.cookies.get('user_name')
    return '%s --- %s' % (user_id, user_name)


@app.route('/login')
def login():
    # 默认判断账号与密码是正确的
    response = make_response('success')
    response.set_cookie('user_id', '1')
    response.set_cookie('user_name', 'gakki', max_age=3600)
    return response


@app.route('/logout')
def logout():
    response = make_response('success')
    response.delete_cookie('user_id')
    return response


if __name__ == '__main__':
    app.run(debug=True)