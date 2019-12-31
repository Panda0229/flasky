from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookie，默认有效期是临时cookie，浏览器关闭就失效
    resp.set_cookie("Itcast", "python")
    resp.set_cookie("Itcast1", "python1")
    # 使用max_age设置有效期，单位为秒
    resp.set_cookie("Itcast2", "python2", max_age=3600)
    # 通过设置响应头来设置cookie
    resp.headers["Set-Cookie"] ="Itcast3=python3; Expires=Sun, 17-Nov-2019 12:51:38 GMT; Max-Age=3600; Path=/"
    return resp


@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("Itcast")
    return c


@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("Itcast1")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
