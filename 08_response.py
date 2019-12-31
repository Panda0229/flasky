from flask import Flask, abort, Response, make_response


app = Flask(__name__)


# 自定义响应信息
@app.route("/index")
def index():
    # 1 使用元组，返回自定义的响应信息
    #           响应体     状态码           响应头
    # return "index page", 400, [("Itcast", "python"), ("City", "HaErBin")]
    # return "index page", 400, {"Itcast": "python1", "City": "HaErBin"}
    # 可以传入非标准的状态码，比如666（状态码只有1-5五个字段）
    # return "index page", 666, {"Itcast": "python1", "City": "HaErBin"}
    # return "index page", "666 itcast status", {"Itcast": "python1", "City": "HaErBin"}
    # 可以不传响应头
    # return "index page", "666 itcast status"

    # 2使用make_response来构造响应体信息
    resp = make_response("index page2")
    resp.status = "999 itcast"  # 设置状态码
    resp.headers["city"] = "HRB"  # 设置响应头
    return resp


if __name__ == "__main__":
    app.run(debug=True)
