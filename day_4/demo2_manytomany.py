from flask import Flask
from flask_sqlalchemy import SQLAlchemy, models_committed

app = Flask(__name__)
app.secret_key = "asdoqiwm"

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jhonchen:2553522375@localhost:3306/manytomany"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# 创建一个单独的表作为辅助表  并且不使用模型  直接定义为普通表
tb_student_course = db.Table(
    "student_course",
    db.Column('student_id', db.Integer, db.ForeignKey("student.id")),
    db.Column('course_id', db.Integer, db.ForeignKey("course.id")),
)


class Student(db.Model):
    # 学生表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 建立关系使表便于查询
    course = db.relationship('Course',
                             backref=db.backref("students", lazy="dynamic"),
                             secondary=tb_student_course)
    '''lazy决定了什么时候加载数据  如果不指定该值  那么当student查询数据之后 course已经有值,
       如果指定该值  那么当student查询数据之后  course并没有值  而只是查询对象,
       如果只是查询对象  那么就可以在用的时候再去数据库查询,避免不必要的操作影响性能,
       lazy="dynamic",  # lazy="subquery"是默认值'''


class Course(db.Model):
    # 课程表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


# 订阅谁发的信号,当信号发出之后,会调用其装饰的函数
@models_committed.connect_via(app)
def db_changed(app, changes):
    print(changes)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 添加测试数据

    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    stu1.courses = [cou2, cou3]
    stu2.courses = [cou2]
    stu3.courses = [cou1, cou2, cou3]

    db.session.add_all([stu1, stu2, stu3])
    db.session.add_all([cou1, cou2, cou3])

    db.session.commit()

    app.run(debug=True)