# 1.导入蓝图类
from flask import Blueprint

# 初始化蓝图对象
cart_blu = Blueprint('cart', __name__, static_folder="static", url_prefix='/cart', template_folder='templates')

from .views import *