from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    my_int = 10
    my_str = '<h1>enheng<h1>'
    my_list = [1, 4, 5]
    my_dict = {
        'da': 1,
        'se': 'asd'
    }
    my_dict_list = [
        {
            "good_name": "大白菜",
            "price": 18,
        },
        {
            "goof_name": "胡萝卜",
            "price": 15,
        }
    ]
    return render_template('demo6_template.html',
                           a=my_int,
                           b=my_str,
                           c=my_list,
                           d=my_dict,
                           e=my_dict_list)


# 自定义过滤器
# 方式1: 装饰器形式
# @app.template_filter('lireverse')
def do_lireverse(li):
    temp = list(li)
    temp.reverse()
    return temp


# 方式2
app.add_template_filter(do_lireverse, 'lireverse')


if __name__ == '__main__':
    app.run(debug=True)