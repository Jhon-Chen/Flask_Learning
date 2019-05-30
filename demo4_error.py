from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/')
def demo1():
    # 主动抛出http指定状态码
    # abort(404)
    a = 0
    b = 1 / a
    return 'demo1'


# 使用装饰器的形式去捕获指定的错误码和异常
@app.errorhandler(404)
def page_not_found(error):
    return "连接丢失 同步失败"


@app.errorhandler(ZeroDivisionError)
def zero_division_error(error):
    return '数据错误 肌体异常'


if __name__ == '__main__':
    app.run(debug=True)