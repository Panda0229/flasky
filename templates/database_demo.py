from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:127.0.0.1:3306/db_python"

    # 设置sqlalchemy自动更新跟踪数据库
    SQLAlchemy_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


# 表名命名规范：
# ihome --》ih_user  数据库名缩写_表名
# tbl_user tbl_表名
# 创建数据库模型类
class Role(db.Model):
    """用户角色表"""
    __tablename__ = "tb_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")


class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    app.run(debug=True)
