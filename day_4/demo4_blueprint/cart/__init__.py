# 1.导入蓝图类
from flask import Blueprint

# 初始化蓝图对象
cart_blu = Blueprint('cart', __name__)

from .views import *