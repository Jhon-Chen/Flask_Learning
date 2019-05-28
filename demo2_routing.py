import json

from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    return 'demo1'

# 给路由添加参数  格式就是<参数名>
# 并且视图函数需要接受这个参数
@app.route('/user/<int:user_id>')
def demo2(user_id):
    return 'demo2 %s' % user_id


@app.route('/demo3', methods=['get', 'post'])
def demo3():
    return 'demo3 %s' % request.method


@app.route('/json')
def demo4():
    json_dict = {
        "name": "gakki",
        "age": 18,
        "appearance": "lovely",
        "user_info": {
            "height": 169,
            "hobby": "sleep"}
    }
    # 使用json.dumps将字典转换成字符串
    # result = json.dumps(json_dict)
    # 使用json.loads将json字符串转成字典
    # test_dit = json.loads('{"name": "gakki","age": 18}')
    # return result

    return jsonify(json_dict)


# 重定向
@app.route('/redirect')
def demo5():

    # return redirect('http://47.100.200.127')
    return redirect(url_for('demo2', user_id=996))


# 返回自定义的状态码
@app.route('/demo6')
def demo6():
    return 'demo6', 666


if __name__ == '__main__':
    app.run(debug=True)
    print(app.url_map)