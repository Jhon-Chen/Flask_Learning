from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# 配置并初始化对象
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@localhost:port/database_name"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)