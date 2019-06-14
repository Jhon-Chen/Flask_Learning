from flask import render_template

from . import cart_blu

# 3.创建蓝图路由
@cart_blu.route('/list')
def cart_list():
    return render_template('cart_html.html')