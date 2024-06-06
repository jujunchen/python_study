# int() 转换为 int 类型
print(int(1.2))

# 如果字符串中有数字和正负号(+/-)以外的字符就会报错
# print(int('1.2')) #报错
print(int('+1'))

# float() 转换为 float 类型
print(float(1))
# 如果字符串中有数字和正负号(+/-)和小数点以外的字符就会报错
# print(float('1.2a')) #报错
print(float('+1.2'))

#str() 转换为字符串类型，任何类型都可以转换成字符串类型
# 浮点数 会去掉小数部分的0
print(str(1.20))

# list() 转换为列表类型,必须是可迭代对象
print(list('abc'))

# 浅拷贝，只拷贝第一层数据
import copy
a = [1,2,3,[4,5,6]]
b = copy.copy(a)
# 拷贝的列表地址不一样
print(id(a))
print(id(b))
# 嵌套列表地址相同
print(id(a[3]))
print(id(b[3]))
# 深拷贝，拷贝所有数据 deepcopy()


