# 1.字符串编码转换
a = '中文'
en = a.encode()
print(en)   # bytes, 以字符为单位进行处理
# 解码
den = en.decode()
print(den)

# 2.字符串拼接
a = 'hello'
b = 'world'
c = a + b
print(c)
print(a, b, sep='-')

# 3.重复输出
print((c + "\n") * 3)

# 4.成员运算符
# 作用：检查字符串中是否包含指定的字符
print('h' in a)  # Ture
print('h' not in a) # False

# 5.字符串下标
# 从右往左，从-1开始
# 从左往右，从0开始
print(a[-1])
print(a[0])

# 6.切片
# 对字符串进行切片
# 字符串切片：字符串[起始位置：结束位置：步长]，不包含最后一位，不写步长，默认是1
# 负数表示从字符串末尾开始
# 默认起始位置为0，结束位置为字符串长度，步长为1
print(a[0:2]) # he
print(a[2:])
print(a[:-1]) # hell
a = 'hello'
print(a[-1:])  #o
# 步长：表示选取间隔，不写步长，则默认是1
# 步长的绝对值大小决定切取的间隔，正负号决定切取方向
# 正数表示从左往右切取，负数表示从右往左切取
print(a[::-1]) # olleh
print(a[::-2]) # olh

# 7.字符串查找
# find() 检测某个字符串是否包含在某个字符串中，返回第一个匹配的位置
print(a.find('l'))
print(a.find('l', 3)) # 在指定范围内查询
# index() 检测某个字符串是否包含在某个字符串中，如果存在就返回这个子字符串在字符串中的位置，如果字符串不存在，则报错
print(a.index('l'))
#print(a.index('l', 4)) # 从下标4开始没有找到
# 同样包前不包后，find 没找到，返回-1,index 没有找到报错

# 8.count() 统计字符串中某个字符出现的次数
print(a.count('l'))
print(a.count('l', 1, 3)) # 在指定范围内查询

# 9.字符串替换
# replace() 替换字符串中的某个字符
print(a.replace('l', 'x'))