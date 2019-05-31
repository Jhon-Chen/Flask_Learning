from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    # abort(520)
    return 'index'


@app.errorhandler(404)
def internal_server_error(e):
    return '海哥崩了'


if __name__ == '__main__':
    app.run(debug=True)