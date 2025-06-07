# isinstance(实例对象, 数据类型) 判断实例对象是否可以迭代

list1 = [1, 2, 3]
print(isinstance(list1, list))

age = 18
print(isinstance(age, int))

for i in age:
    print(i)


# 创建可迭代对象
# iter() 创建可迭代对象, next() 获取可迭代对象中的下一个元素 

class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration 


for item in MyIterable([1,2,3]):
    print(item)

# 可迭代对象: Iterable 和 迭代器对象： Iterator
