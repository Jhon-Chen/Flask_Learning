from flask import Flask
from werkzeug.routing import BaseConverter


class RegexConvert(BaseConverter):
    # 自定义正则的转换器
    # regex = "[0-9]{6}"
    def __init__(self, url_map, *args):
        super(RegexConvert, self).__init__(map)
        # 取到下标为o的参数给regex赋值
        self.regex = args[0]


app = Flask(__name__)
# 将自己的转换器添加到默认的转换器列表中
app.url_map.converters["my_convert"] = RegexConvert


@app.route('/')
def index():
    return 'index'


# 规则：/user/六位数字  //[0-9]{6}
# 自定义转换器
@app.route('/user/<my_convert:user_id>')
def demo1(user_id):
    return '用户id是 %s' % user_id


if __name__ == '__main__':
    app.run(debug=True)
