from flask import Flask, request


app = Flask(__name__)


# 接口 api
# 127.0.0.1:5000/index?city=shenzhen&country=china 问号后面的成为查询字符串(QueryString)
@app.route("/index", methods=["GET", "POST"])
def index():
	# request中包含了前端发送过来的所有请求数据
	# form和data是用来提取请求中的数据
	# 通过request.form可以直接提取请求中的表单格式的数据，是一个类字典的对象
	# 通过get方法只能拿到多个同名参数中的一个
	name = request.form.get("name")
	age = request.form.get("age")
	# 通过getlist可以提取到表单中的重复部分
	name_li = request.form.getlist("name")

	# 如果请求体的数据不是表单格式（如json）格式，可以通过request.data获取
	print("request.data: %s " % request.data)

	# args是用来提取url中查询字符串的参数
	city = request.args.get("city")

	return "hello name=%s, age=%s, city=%s, name_li=%s" % (name, age, city, name_li)


if __name__ == "__main__":
	app.run(debug=True)
