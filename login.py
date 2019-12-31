from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    # 接收参数
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    # 参数判断
    # "" 0 [] () {} None在逻辑判断时都为假
    if not all([user_name, password]):
        # 表示name或password中有一个为空或者都为空
        resp = {
            "code": 1,
            "message": "invalid params"
        }
        return jsonify(resp)

    if user_name == "admin" and password == "python":
        resp = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "wrong user name or password"
        }
        return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)
