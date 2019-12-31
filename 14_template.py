from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "python",
        "age": 18,
        "my_dict": {"city": "HRB"},
        "my_list": [1, 2, 3, 4, 5],
        "my_int": 0
    }
    return render_template("index.html", **data)
    # return render_template("index.html", name="python", age=18)


# 自定义过滤器
# 方法一
def li_step2(li):
    """自定义过滤器"""
    return li[::2]


# 注册过滤器,参数分别为定义过滤器的函数和过滤器的名称
app.add_template_filter(li_step2, "li2")


# 方法二
@app.template_filter("li3")
def li_step3(li):
    return li[::3]


if __name__ == "__main__":
    app.run(debug=True)
