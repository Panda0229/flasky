from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 应用现有的转换器
# 转换器：int、float、path(和默认相似，包括/)
# @app.route('/goods/<goods_id>') 不加转换器默认字符串
# 127.0.0.1:5000/goods/123
@app.route('/goods/<int:goods_id>')
def goods_detail(goods_id):
    return "goods detail page %s" % goods_id


# 1 定义自己的转换器(正则)
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super().__init__(url_map)
        self.regex = r'1[3895]\d{9}'


class RegexConverter(BaseConverter):
    """定义正则转换器"""
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性进行路由匹配
        self.regex = regex

    def to_python(self, value):
        """在完成匹配后自动执行，将匹配结果进行处理返回到mobile中"""
        print("to_python方法被调用")
        # value就是匹配完成之后的值
        return value

    def to_url(self, value):
        """使用url_for方法的时候会被调用"""
        print("to_url 方法被调用")
        return "13199572290"


# 2 将定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] = MobileConverter


# 3 127.0.0.1:5000/send/13199572290
@app.route("/send/<re(r'1[3589]\d{9}'):mobile>")
def send_sms(mobile):
    return "send sms to %s " % mobile


@app.route("/sendto/<mobile:mobile_num>")
def send_sms_mobile(mobile_num):
    return "send sms to %s" % mobile_num


@app.route("/index")
def index():
    url = url_for("send_sms", mobile=13199572291)
    print(url)
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    # app.run()
    app.run(debug=True)


