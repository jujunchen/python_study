# def 定义函数
def say_hello():
    print("hello")

say_hello()

# 函数返回值
def say_hello():
    return "hello", 20

print(say_hello()) # 多个返回元组 一个返回当前值 没值返回None

# 可变参数
# 传入的值的数量是可以改变的，可以传入多个，也可以不传
# def func(*args)


# 关键字参数,以字典形式接收
# def func(**kwargs)

# 函数嵌套调用
# 在一个函数里面调用另外一个函数
def func1():
    print("func1")

def func2():
    func1()
    print("func2")
func2()

# 嵌套定义
# 在一个函数中定义另外一个函数
def func3():
    def func4():
        print("func4")
    func4()
    print("func3")
func3()

# 作用域，全局变量和局部变量
# 全局变量使用global关键字声明

#nonlocal 引用外部函数的变量，只能在嵌套函数中使用，嵌套函数中赋值，会改变外部变量的值，只能修改上一级函数
a = 10
def outer():
    a = 20
    def inner():
        # nonlocal a
        a = 30
        print(a)
    inner()
    print(a)

outer()

# 函数默认参数，为参数提供默认值，可不传，但所有的位置参数必须出现在默认参数前，包括函数顶级和调用
def func5(a, b=10):
    print(a, b)

func5(1)
func5(1, 2)

# 可变参数
def func6(*args):
    print(args)
    print(type(args)) # 元组形式

func6(1,2,3,4,5)

# 关键字参数
def func7(**kwargs):
    print(kwargs) # 字典形式

func7(a=1, b=2)

# 匿名函数
# lambda 参数列表: 函数体

func8 = lambda a, b: a + b
print(func8(1, 2))