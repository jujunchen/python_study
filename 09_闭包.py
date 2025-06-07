# 什么是闭包
"""
闭包：
    1、函数嵌套
    2、返回一个函数
    3、内部函数引用外部函数的变量
"""
def outer():
    # 闭包
    def inner():
        print("hello world")

    return inner