from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/xss", methods=["GET", "POST"])
def xss():
    text = ""
    if request.method == "POST":
        text = request.form.get("text")

    return render_template("xss.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)


# xss是注入攻击
# 当将输入的内容直接放在body中时，如果输入的是一个html语句，
# 在不启用转义的情况下，模板会执行输入的语句。浏览器都默认开启转义
# 当确定所输入为安全时，可以启用safe过滤器
