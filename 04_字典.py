# 字典
# 键值对，键值之间用:，键值对之间用,隔开
dic = {'name': '张三', 'age': 18, 'sex': '男'}
print(dic)

print(dic['name'])
print(dic.get('name'))
print(dic.get('age1')) #键名不存在
print(dic.get('age1', 20)) # 键名不存在，返回20

# 列表通过下标修改，字典通过键名修改
dic['name'] = '李四'
print(dic)

# 没有键名，会新增
dic['address'] = '北京'
print(dic)
dic['address'] = '杭州'
print(dic)

# 删除
del dic['name']
# del dic  # 删除字典
print(dic)

# 删除指定键值对，健不存在会报错
# dic.pop('age1') # 报错
dic.pop('age')
print(dic)

dic.popitem() # 3.7以后删除最后一个元素
print(dic)

# keys 返回所有键
# values 返回所有值
# items 返回键值对
print(dic.items())

# 集合 set
# 空集合 s = set()
# 空字典 d = {}
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#集合无序的实现方式涉及hash表，int整型的hash值就是本身，字符串的hash值就是字符串的ASCII码值之和
# 不能改变集合中的值
s = {'张三', '李四', '王五', '张三'}
print(s)

# 默认删除根据hash表排序后的第一个元素
s = {'a', 'c', 'b'}
print(s)
s.pop()
print(s)

# discard 删除指定元素
s.discard('a')
print(s)

# remove 删除指定元素，没有指定元素会报错
# s.remove('b')
print(s)

# 集合运算
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 并集
print(s1 | s2)
print(s1.union(s2))

# 交集
print(s1 & s2)