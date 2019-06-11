from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jhonchen:2553522375@localhost:3306/booktest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'asfzxcqwe'


class AddBookForm(FlaskForm):
    author = StringField('作者', validators=[InputRequired('请输入作者')])
    book = StringField('图书', validators=[InputRequired('请输入书名')])
    submit = SubmitField("添加")


db = SQLAlchemy(app)


# 定义模型  一对多模型
class Author(db.Model):
    # 作者模型　"一"
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 定义属性,以便作者模型可以直接通过该属性访问其"多"的一方的数据
    # backref给Book也添加了一个author的属性,使其可以反过来获取"一"这一方的信息
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    # 书本模型  "多"
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 先把"一"的一方的"id"作为"多"的外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    try:
        book = Book.query.get(book_id)
    except Exception as e:
        print(e)
        return "查询错误"
    if not book:
        return "书籍不存在"
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return "删除失败"
    return redirect(url_for('index'))


@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    try:
        author = Author.query.get(author_id)
    except Exception as e:
        print(e)
        return "查询错误"
    if not author:
        return "作者不存在"

    # 删除作者及其作品
    # 先删除作品 再删除作者
    try:
        Book.query.filter(Book.author_id == author_id).delete()
        db.session.delete(author)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return "删除失败"
    return redirect(url_for('index'))


@app.route('/', methods=['get', 'post'])
def index():
    # 返回首页
    book_form = AddBookForm()

    # 如果book_form可以被提交
    if book_form.validate_on_submit():
        # 取出表单中的数据
        # 第一种方式
        # author_name = request.form.get('author')
        # book_name = request.form.get('book')

        # 第二种方式
        author_name = book_form.author.data
        book_name = book_form.book.data

        # 做具体业务逻辑的实现

        # 查询指定名字的作者是否存在
        author = Author.query.filter(Author.name == author_name).first()
        # 如果没有这个作者 那就新建作者
        if not author:
            try:
                # 添加作者信息到数据库(指定其作者)
                # 作者的模型对象
                author = Author(name=author_name)
                db.session.add(author)
                db.session.commit()
                # 添加书籍信息到数据库(指定其作者)
                book = Book(name=book_name, author_id=author.id)
                db.session.add(book)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                flash("添加失败")
        # 如果已经有这作者 那就在下边直接添加
        else:
            book = Book.query.filter(Book.name == book_name).first()
            if not book:
                try:
                    # 添加书籍信息到数据库
                    book = Book(name=book_name, author_id=author.id)
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    print(e)
                    flash("添加失败")
            else:
                flash("已存在")
    else:
        if request.method == "POST":
            flash('参数错误')

    # 查询数据
    authors = Author.query.all()
    # 将数据传入模板中
    return render_template('demo1_book.html', authors=authors, form=book_form)


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