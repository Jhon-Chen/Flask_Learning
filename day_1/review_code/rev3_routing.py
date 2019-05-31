from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/user/<int:user_id>')
def user_info(user_id):
    return "%s" % user_id


if __name__ == '__main__':
    app.run(debug=True)
