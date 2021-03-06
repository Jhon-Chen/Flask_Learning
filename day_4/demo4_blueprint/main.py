from flask import Flask
from demo4_blueprint.order import order_blu
from demo4_blueprint.cart import cart_blu

app = Flask(__name__)

# 3.把蓝图注册到app上
app.register_blueprint(order_blu)
# 4.把蓝图注册到app上
app.register_blueprint(cart_blu)


@app.route('/')
def index():
    return 'index'


# 订单列表
"""以下代码抽取到order.py中
@app.route('/order/list')
def order_list():
    return 'order_list'
"""


@app.route('/user/info')
def user_info():
    return "user_info"


"""以下标签拷贝到cart模块中
@app.route('/cart/list')
def cart_list():
    return "cart_list" 
"""


if __name__ == '__main__':
    app.run(debug=True)