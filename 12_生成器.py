# 什么是生成器
#  生成器是一个特殊的迭代器，生成器函数用def定义，生成器函数用yield定义

def func1():
    yield 1
    yield 2
    yield 3

num = func1();
print(next(num))

for i in func1():
    print(i)