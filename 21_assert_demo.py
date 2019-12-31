def num_div(num1, num2):
    # assert 断言，后面是一个表达式，如果表达式返回为真，则断言成功，程序能够继续往下执行
    # 如果表达式返回为假，则断言失败，assert会抛出异常AssertionError，终止程序
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0

    print(num1 / num2)


if __name__ == '__main__':
    num_div(100, 5)
