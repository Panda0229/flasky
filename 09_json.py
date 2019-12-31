from flask import Flask, jsonify
import json


app = Flask(__name__)


# 自定义响应信息
@app.route("/index")
def index():
    # json就是字符串
    data = {
        "name": "zhangsan",
        "age": 24
    }

    # json.dumps(字典),将python字典转换为字符串
    # json.loads(字符串),将python字符串字典转换为字典

    # json_str = json.dumps(data)
    # return json_str, 200, {"Content-type": "application/json"}

    # 使用Flask中的jsonify来将字典转换成json,并设置响应头content-type为application/json
    # return jsonify(data)
    return jsonify(city="HRB", country="china")


if __name__ == "__main__":
    app.run(debug=True)
