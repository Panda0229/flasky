from flask import Flask, abort, Response


app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    name = ""
    pwd = ""
    if name != "zhangsan" or pwd != "admin":
        # 使用abort函数可以立即终止视图函数的执行
        # 并可以返回给前段特定的信息
        # 1 传递状态码的信息，必须是标准的http状态码
        abort(404)

        # 2 传递响应体信息
        # resp = Response("login failed")
        # abort(resp)

    return "login success"


# 自定义错误处理方法
@app.errorhandler(404)
def handle_404_error(err):
    """自定义的处理错误方法"""
    # 这个函数返回值会是前段用户看到的最终结果
    return "出现了404错误，错误信息 %s " % err


if __name__ == "__main__":
    app.run(debug=True)
