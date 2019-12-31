from flask import Blueprint

# 创建一个蓝图, 在蓝图中，需要指明模板文件的文件夹,也可以放在主文件的templates中，如果蓝图中和主文件的
# templates中都有模板，则以主目录中的为主
app_cart = Blueprint("app_cart", __name__, template_folder="templates")

# 在 __init__.py 文件被执行的时候，把视图加载进来。让蓝图与应用程序知道视图的存在
from .views import get_cart
