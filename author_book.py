from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/author_book"

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "secret_key"


app.config.from_object(Config)
# 创建sqlalchemy的数据库连接对象
db = SQLAlchemy(app)

# 创建flask脚本管理工具对象
manager = Manager(app)

# 创建数据库迁移工具对象
Migrate(app, db)

# 向manager对象中添加数据库的操作命令
manager.add_command("db", MigrateCommand)


# 定义数据库的模型
class Author(db.Model):
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")
    emails = db.Column(db.String(64))
    mobil = db.Column(db.String(64))


class Book(db.Model):
    __tablename__ = "tbl_book"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


# 创建表单模型类
class AuthorBookForm(FlaskForm):
    """作者数据模型类"""
    author_name = StringField(label="作者姓名", validators=[data_required("作者必填")])
    book_name = StringField(label="书籍名称", validators=[data_required("必填")])
    submit = SubmitField(label="提交")


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        # book = Book(name=book_name, author_id=author.id)
        book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)


# post  /delete_book  json
# {"book_id":x}
@app.route("/delete_book")
def delete_book():
    """删除数据"""
    # 提取参数
    # 如果前端发送的是json数据格式，get_json会解析成字典
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify(conde=0, message="OK")


# /delete_book_get?book_id=xx
@app.route("/delete_book_get", methods=["GET"])
def delete_book_get():
    """删除数据"""
    # 提取参数
    # 如果前端发送的是json数据格式，get_json会解析成字典
    book_id = request.args.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
    # bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # db.session.commit()
    # app.run(debug=True)

    # 通过manager启动程序
    manager.run()


# 1002  python author_book.py db init     初始化，会在程序根目录下生成一个migrations的文件夹
# 1003  python author_book.py db migrate  数据库迁移
# 1006  python author_book.py db upgrade  提交
# 1007  python author_book.py db migrate -m "add mobil "  为每次的更改进行标注
# 1010  python author_book.py db history  查询历史操作
# python author_book.py db downgrade 12b2d39f6d72  回退回指定的版本

