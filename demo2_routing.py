from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    return 'demo1'


if __name__ == '__main__':
    app.run(debug=True)