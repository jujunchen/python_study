# 1、算术运算符
# 取整除，取商的整数部分，向下取整
# 向下取整，不管四舍五入的规则，只要后面又小数，就忽略小数
a = 5
b = 3
print(a // b)
# % 取余数，只取余数部分
print(a % b)
# ** 取幂 m**n = m的n次方
print(2 ** 3)
# 使用算术运算符，有浮点数，结果为浮点数
print(6.0 / 3)
# 算术运算符优先级：** > * / // % + -

# 2、赋值运算符
# = 用来给变量赋值
a = 10
# 将运算的值赋值给变量
a = a + 10
print(a)
# += -= -= 
a = 10
a += 10
print(a)
# print(10+=3) 存数字不能用于赋值运算符

# 3、输入函数
# print(input("请输入"))

# 4、转义字符
# \t 制表符
print("hello\tworld")
# \n 换行
print("hello\nworld")
# \r 回车，表示将当前位置移到本行开头
print("hello\rworld")
# \b 退格
# print("hello\bworld")
# \f 换页
# print("hello\fworld")
# \\' 单引号
# print("hello\\'world")
# \\" 引号
# r br 字符串的原始形式，不进行转义
print(r"hello\'world")

# 5、比较运算符
# == 比较两个变量的值是否相等  != 比较两个变量的值是否不相等 >  >= < <=
# 6、逻辑运算符
# and 与 or 或 not 非
