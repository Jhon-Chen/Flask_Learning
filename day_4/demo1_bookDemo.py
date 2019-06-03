from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jhonchen:2553522375@localhost:3306/booktest"
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 定义模型  一对多模型
class Author(db.Model):
    # 作者模型　"一"
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 定义属性,以便作者模型可以直接通过该属性访问其"多"的一方的数据
    # backref使其可以反过来获取"一"这一方的信息
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    # 书本模型  "多"
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # "一"的一方的"id"作为外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # 创建表
    db.drop_all()
    db.create_all()
    # 添加数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()


    app.run(debug=True)