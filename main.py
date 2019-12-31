from flask import Flask
from orders import app_orders
from cart import app_cart

app = Flask(__name__)

# 注册蓝图
# app.register_blueprint(app_orders)
#                                    前缀
app.register_blueprint(app_orders, url_prefix='/orders')
app.register_blueprint(app_cart, url_prefix='/cart')


@app.route("/")
def index():
    return "index page"


if __name__ == '__main__':
    app.run(debug=True)
