from flask import Flask, current_app

# Flask是一个类，创建一个Flask的应用对象
# __name__表示当前的模块名字
# flask已当前文件模块存在的目录为根目录,默认目录中的static为静态目录，templates为模板目录
# __name__所在的模块为启动模块时，打印出来的为__main__，作为包被导入时，打印出来的为它所在模块的名字
app = Flask(
	__name__,
	static_url_path="/python",  # 访问静态资源的URL前缀，默认值为static
	static_folder="static",  # 静态资源的目录，默认就是static
	template_folder="templates",  # 模板文件的目录，默认就是templates
			)

# @app.route('/')
# def index():
# 	return '<h1>hello world!<h1>'

# 配置参数的使用方式
# 1 使用配置文件
# app.config.from_pyfile("config.cfg")


# 2 使用对象配置参数
class Config(object):
	DEBUG = True
	ITCAST = "python"


app.config.from_object(Config)

# 3 直接操作config的字典对象
# 多个对象：
# app.config.update(
# 	k1 = 1,
# 	k2 = 2,
# )
# app.config["DEBUG"] = True


@app.route('/user/<name>')
def index(name):
	# a = 1/0
	# 在视图函数中读取配置参数
	# 1 直接从app的config字典中取值
	print(app.config.get("ITCAST"))

	# 2 通过current_app获取参数(适用于视图函数不能直接调用app函数的情况)
	# print(current_app.config.get("ITCAST"))

	return "<h1>Hello,{}!<h1>".format(name)


if __name__ == '__main__':
	# app.run()
	app.run(host="0.0.0.0", port=5000)

