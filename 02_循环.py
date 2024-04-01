# 1、while循环体
# while 条件:
#     循环体
#     改变变量

# 2、for循环体
# for 循环变量 in 可迭代对象:
#     循环体
#     改变变量

# 3、range()函数，range里面只写一个数，就是循环的次数，默认从0开始
# range(开始, 结束, 步长)
for i in range(1, 10):  # 包前不包后
    print(i)

# 4、break 语句，跳出循环
# 5、continue 语句，跳过本次循环
# 6、成员运算符，in 包含返回true，不包含返回false
    # not in 不包含返回true, 包含返回false
# 7、切片，指对操作的对象截取其中一部分的操作
    # 语法：[开始:结束:步长]
    # 包前不包后
st = "hello world"
print(st[0:4])