# 示例：is 和 == 的区别

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print('a == b ->', a == b)   # True，因为内容相等
print('a is b ->', a is b)   # False，因为不是同一个对象

print('a == c ->', a == c)   # True，内容相等
print('a is c ->', a is c)   # True，因为 c 引用的是同一个对象

# 对于不可变类型，== 和 is 有时会表现相似，但含义不同
x = 256
y = 256
print('x == y ->', x == y)   # True
print('x is y ->', x is y)   # 可能为 True，因为小整数缓存

x = 257
y = 257
print('x == y ->', x == y)   # True
print('x is y ->', x is y)   # 可能为 False，解释器不会缓存较大整数
