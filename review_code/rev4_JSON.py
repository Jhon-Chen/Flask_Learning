from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    json_dict = {
        "abc": 16,
        "name": "gakki"
    }
    return jsonify(json_dict)


if __name__ == '__main__':
    app.run(debug=True)