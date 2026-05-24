# lambda 示例程序

# 简单的 lambda 表达式，计算两个数的和
add = lambda x, y: x + y
print('add(3, 5) =', add(3, 5))

# 用 lambda 和 map 处理列表
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n * n, numbers))
print('squared =', squared)

# 用 lambda 和 filter 过滤列表中的偶数
evens = list(filter(lambda n: n % 2 == 0, numbers))
print('evens =', evens)

# 用 lambda 和 sorted 按长度排序字符串列表
words = ['apple', 'banana', 'kiwi', 'orange']
sorted_words = sorted(words, key=lambda s: len(s))
print('sorted_words =', sorted_words)