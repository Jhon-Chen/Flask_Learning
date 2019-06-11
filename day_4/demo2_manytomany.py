from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "asdoqiwm"

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jhonchen:2553522375@localhost:3306/manytomany"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    course = db.relationship('Course', backref="students", secondary=tb_student_course)


class Course(db.Model):
    # 课程表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)






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