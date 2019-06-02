from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# 配置并初始化对象
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jhonchen:2553522375@127.0.0.1:3306/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)