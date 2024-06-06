# 1. 列表
# 列表名 = [元素1, 元素2, 元素3...]
list1 = [1, 2, 3, 4, 5]
print(list1)
# 切片操作
print(list1[0:2])

# 2. 列表的常用操作
# 2.1 添加元素
list1.append(6)
print(list1)
list1.insert(0, 0)
print(list1)
# 2.2 删除元素
list1.pop() # 默认删除最后一个元素
print(list1)
list1.pop(0) # 删除指定位置的元素
print(list1)
list1.remove(1) # 删除指定元素的第一个
print(list1)
list1.remove(5)
print(list1)
list1.extend([7, 8, 9])
print(list1)
del list1[0] # 删除指定位置的元素
print(list1)

# 2.3 查找元素
# in 判断元素是否存在列表中，存在true,不存在false
# not in 判断元素是否不存在列表中，不存在true,存在false
print(1 in list1)
print(10 not in list1)

# index 返回指定数据所在位置的下标，如果查找的数据不存在就会报错
# count 返回指定数据出现的次数

# sort 排序,默认从小到大
list1 = [1, 3, 2, 5, 4]
# list1.sort()
print(list1)

# reverse 列表反转
list1.reverse()
print(list1)

# 列表遍历，in 后面可以放列表，也可以放range()，迭代对象
# for i in list1:
#     print(i)

[print(i) for i in list1]

# 列表嵌套
list2 = [1, 2, 3, 4, 5, [6,7]]
print(list2[5][0])