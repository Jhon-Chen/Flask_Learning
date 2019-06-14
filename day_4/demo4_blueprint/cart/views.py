from . import cart_blu

# 3.创建蓝图路由
@cart_blu.route('/cart/list')
def cart_list():
    return "cart_list"