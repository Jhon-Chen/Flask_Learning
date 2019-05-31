from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/cookie')
def set_cookie():
    respon = make_response('this is setting cookie')
    respon.set_cookie('username', 'jhonchen', max_age=1200)
    return respon


@app.route('/request')
def get_cookie():
    resp1 = request.cookies.get('username')
    return resp1


if __name__ == '__main__':
    app.run(debug=True)