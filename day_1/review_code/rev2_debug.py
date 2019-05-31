from flask import Flask


class Config(object):
    DEBUG = True


app = Flask(__name__)
# app.config.from_object(Config)
app.config.from_pyfile('config.ini')


@app.route('/')
def index():
    return 'macbookpro'


if __name__ == '__main__':
    app.run(debug=True)