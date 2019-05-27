# 导入flask
from flask import Flask

# 创建flask应用程序
app = Flask(__name__)

# 使用装饰器路由与视图函数关联
@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
