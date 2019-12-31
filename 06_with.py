# 上下文管理器
# with open("./1.txt", "w") as f:
#     f.write("hello flask")
#     f.write("hello flask")
#     f.write("hello flask")


# 使用with会自动调用两个函数
class Foo(object):
    def __enter__(self):
        """进入with语句时被with调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句时被with调用"""
        print("exit called")
        print("exc_type: %s " % exc_type)
        print("exc_val: %s " % exc_val)
        print("exc_tb: %s " % exc_tb)


with Foo() as foo:
    print("hello python")
    # with在执行过程中有异常的情况下，会终端执行，直接调用__exit__方法的内容
    a = 1 / 0
    print("hello end")


# 使用with进行文件操作不会因为没有进行文件关闭操作而报出异常，会自动调用__exit__
