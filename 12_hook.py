from flask import Flask, request, url_for


app = Flask(__name__)


@app.route("/hello")
def hello():
    print("hello flask")
    return "hello page"


@app.route("/index")
def index():
    print("index被执行")
    return "index page"


@app.before_first_request
def handle_before_first_request():
    """在第一次请求之前被执行"""
    print("handle_before_first_request被执行")


@app.before_request
def handle_before_request():
    """在每次请求之前被执行"""
    print("handle_before_request被执行")


@app.after_request
def handle_after_request(response):
    """在每次请求（视图函数处理）之后被执行，前提是视图函数没有出现异常"""
    print("handle_after_request被执行")
    return response


@app.teardown_request
def handle_teardown_request(response):
    """在每次请求 (视图函数处理)之后都被执行， 无论视图函数是否出现异常，都被执行, 工作在非调试模式时 debug=False"""
    path = request.path
    if path == url_for("index"):
        print("在请求钩子中判断请求的视图逻辑: index")
    elif path == url_for("hello"):
        print("在请求钩子中判断请求的视图逻辑: hello")
    print("handle_teardown_request 被执行")
    return response


if __name__ == "__main__":
    app.run()
