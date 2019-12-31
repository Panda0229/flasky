from flask import Flask
from flask_script import Manager  # 启动命令的管理类


app = Flask(__name__)

# 通过Manage管理类的对象
manager = Manager(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == "__main__":
    # app.run(debug=True)
    # 通过管理类对象启动Flask
    manager.run()


# flask-script库
# 1、简介
# 简单来说，就是一个flask终端启动参数解析工具；这样我们就可以不更改代码完成不同方式的启动。
# 2、使用
# 1）导入类库：from flask_script import Manager
# 2）创建对象：manager = Manager(app)
# 3）启动代码：if __name__ == '__main__':
#       　　　　　　　manager.run()
# 4）终端启动：python manage.py runserver -d -r -h 0.0.0.0 -p 5000
# 3、启动参数说明
# 1）-h, --host    指定主机
# 2）-p, --port    指定端口
# 3）-d         开启调试模式
# 4）-r        代码修改后自动加载
# 5）-?, --help    查看帮助信息
