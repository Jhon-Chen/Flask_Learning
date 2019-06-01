from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/demo1')
def demo1():
    return render_template('temp1_macro.html')


if __name__ == '__main__':
    app.run()
