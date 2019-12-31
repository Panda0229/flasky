from flask import Flask, request


app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    """接收前段传来的图片"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        return "未上传文件"

    # 将接收到的文件保存到本地
    # 1 创建一个新文件
    # f = open("./demo.jpg", "wb")
    # 2 向文件中写内容
    # data = file_obj.read()
    # f.write(data)
    # 3 关闭文件
    # f.close()
    # return "上传成功"

    # 直接使用上传的文件对象保存
    file_obj.save("./demo1.jpg")
    return "上传成功"


if __name__ == "__main__":
    app.run(debug=True)
