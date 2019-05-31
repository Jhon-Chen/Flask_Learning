from flask import Flask
from flask_script import Manager
app = Flask(__name__)
# 需求: 可以通过命令行在运行时指定运行的端口
# 创建manager
manager = Manager(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # 使用manager运行
    manager.run()

