#coding=utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
# MigrateCommand : 迁移的命令
from flask_script import Manager


"""
操作顺序:
1.python3 文件 db init
2.python3 文件 db migrate -m"注释"
3.python3 文本 db upgrade 更新至本地版本
4.根据需求修改模型
5.python3 文本 db migrate -m"注释"
6.pyhton3 文本 db upgrade 再次更新
7.若返回版本 则利用 python3 文件 db history 查看版本号 
8.python 文件 db downgrade 版本号 
"""


# 总结迁移的命令：
# 1. 迁移初始化(生成迁移所需要文件夹 migrations) python xxxx.py db init
# 2. 生成迁移版本文件 python xxxx.py db migrate -m "initial"
# 3. 执行迁移(往上迁移) python xxxx.py db upgrade

app = Flask(__name__)
app.secret_key = "asdqe"

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jhonchen:2553522375@localhost:3306/migratetest"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)

# 使用迁移类将应用和数据库连接对象保存起来
Migrate(app, db)
# 创建终端命令的对象
manager = Manager(app)
# 将数据库的迁移命令添加到manager中
manager.add_command('aaa', MigrateCommand)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64), unique=True)
    # 标题
    title = db.Column(db.String(64))
    us = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()

