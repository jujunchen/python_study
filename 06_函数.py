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