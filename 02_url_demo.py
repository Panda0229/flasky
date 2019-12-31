from flask import Flask, redirect, url_for

# Flask是一个类，创建一个Flask的应用对象
# __name__表示当前的模块名字
# flask已当前文件模块存在的目录为根目录,默认目录中的static为静态目录，templates为模板目录
# __name__所在的模块为启动模块时，打印出来的为__main__，作为包被导入时，打印出来的为它所在模块的名字
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello,world!"


# 通过methods限定访问方式
@app.route('/post_only', methods=["POST", "GET"])
def post_only():
    return "hahahuahua"


# 同一个路由装饰多个视图函数，只有在访问路径与访问方式都相同的情况下，第一个视图函数才会完全覆盖第二个视图函数
@app.route("/hello1", methods=["POST"])
def hello1():
    return "hello1"


@app.route('/hello2', methods=["GET"])
def hello2():
    return "hello2"


# 多个装饰器装饰同一个视图函数
@app.route('/hi1')
@app.route('/hi2')
def hi():
    return "hi page"


@app.route('/login')
def longin():
    # url = "/"
    # 使用url_for进行url反转，根据地址推出url
    url = url_for("hello2")
    # redirect是url跳转
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    # app.run()
    app.run(debug=True)
