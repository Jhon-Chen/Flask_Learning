from flask import Flask

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    # 在第一次访问之前会访问这个函数   比如连接数据库的操作
    print('before first request')


@app.before_request
def before_request():
    # 每次请求前都会被调用   比如访问权限的检查
    print('没有绝望的人')


@app.after_request
def after_request(response):
    # 在每次请求之后会诶调用 并且函数里面接受一个参数（响应） 需要返回响应
    print('感同身受只是谎言')
    # 可以在此函数中对响应数据做统一的处理
    return response


@app.teardown_request
def tear_down(error):
    # 在请求之后会被调用 如果请求的函数报出异常 会把具体的异常传入次函数
    print('并不感兴趣')


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)