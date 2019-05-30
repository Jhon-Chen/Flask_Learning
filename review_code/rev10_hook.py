from flask import Flask

app = Flask(__name__)


@app.before_first_request
def before():
    print("恶龙咆哮")


@app.before_request
def before():
    print("实力卖萌")


@app.after_request
def after(response):
    print("陪玩小姐姐")
    return response


@app.teardown_request
def error(e):
    print("你被击杀了")


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    return "啊呜啊呜呜"


if __name__ == '__main__':
    app.run(debug=True)