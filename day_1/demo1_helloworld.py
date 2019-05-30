# coding=utf-8
# 导入flask
from flask import Flask

# 创建flask应用程序
# 第一个参数指代Flask所对应的模板， 其可以决定静态文件从哪个文职开始找
app = Flask(__name__,
            static_url_path='/static',  # 表示静态文件访问的路径
            static_folder='static',  # 表示静态文件所存放的目录 默认值是static
            template_folder='templates'  # 表示模板文件存放的目录
            )


# =====从对象中加载配置=====#
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)

# =====从文件中加载配置=====#
# app.config.from_pyfile('config.ini')

# =====从环境变量中加载配置=====#
# app.config.from_envvar('ENVCONFIG')

# 一些常用的配置 可以直接通过app.的形式设置
app.debug = True
app.config['DEBUG'] = True
# 使用装饰器路由与视图函数关联
@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
