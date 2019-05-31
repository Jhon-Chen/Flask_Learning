from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo2')
def demo2():
    return redirect('http://47.100.200.127')


if __name__ == '__main__':
    app.run(debug=True)