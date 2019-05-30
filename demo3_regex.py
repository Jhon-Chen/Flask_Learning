from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter


class RegexConvert(BaseConverter):
    # 自定义正则的转换器
    # regex = "[0-9]{6}"
    def __init__(self, url_map, *args):
        super(RegexConvert, self).__init__(map)
        # 取到下标为o的参数给regex赋值
        self.regex = args[0]


class ListConverter(BaseConverter):
    # 自己定义转换器
    regex = "(\\d+,?)+\\d$"

    def to_python(self, value):
        # 当匹配到参数之后 对参数做进一步处理之后 再返回给视图函数
        return value.split(',')

    def to_url(self, value):
        # 使用url_for的时候， 对视图函数传的参数进行处理
        # 处理完毕之后以便能够进行路由匹配
        # return "1, 2, 3, 8"
        result = ','.join(str(v) for v in value)
        return result


app = Flask(__name__)
# 将自己的转换器添加到默认的转换器列表中
app.url_map.converters["my_convert"] = RegexConvert
app.url_map.converters["list"] = ListConverter


@app.route('/')
def index():
    return 'index'


# 规则：/user/六位数字  //[0-9]{6}
# 自定义转换器
@app.route('/user/<my_convert("[0-9]{6}, "aaaa""):user_id>')
def demo1(user_id):
    return '用户id是 %s' % user_id


@app.route('/user/<user_ids>')
def demo2(user_ids):
    # 如何才能在视图函数中接受道德user__id就是一个列表
    return "用户的id列表是 %s" % user_ids


@app.route('/demo3')
def demo3():
    return redirect(url_for('demo2', user_id=[1, 3, 5, 9, 7]))


if __name__ == '__main__':
    app.run(debug=True)
