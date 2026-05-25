
"""示例：常用 functools 函数

包含：partial, lru_cache, wraps, total_ordering, singledispatch, cmp_to_key, cached_property
"""
from functools import partial, lru_cache, wraps, total_ordering, singledispatch, cmp_to_key, cached_property
from functools import update_wrapper
import time


# 1. partial: 固定部分参数，生成新的可调用对象
def power(base, exponent):
	return base ** exponent  # 计算 base 的 exponent 次方

square = partial(power, exponent=2)
cube = partial(power, exponent=3)


# 2. lru_cache: 结果缓存（适合纯函数）
@lru_cache(maxsize=128)
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)


# 3. wraps / update_wrapper: 在装饰器中保留原函数元数据
def my_decorator(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		print(f"calling {fn.__name__}")
		return fn(*args, **kwargs)
	return wrapper


# 4. total_ordering: 通过少量比较方法填充其余比较操作
@total_ordering
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __eq__(self, other):
		return self.age == other.age

	def __lt__(self, other):
		return self.age < other.age


# 5. singledispatch: 根据第一个参数类型分发实现不同实现
@singledispatch
def fun(arg):
	return f"default: {arg!r}"


@fun.register(int)
def _(arg: int):
	return f"int: {arg}"


@fun.register(str)
def _(arg: str):
	return f"str: {arg}"


# 6. cmp_to_key: 将旧式比较函数转换为键函数
def cmp(a, b):
	return (a > b) - (a < b)


# 7. cached_property (Python 3.8+): 将方法变为只计算一次的属性
class Data:
	def __init__(self, x):
		self.x = x

	@cached_property
	def expensive(self):
		time.sleep(0.1)
		return self.x * 2


if __name__ == '__main__':
	print('partial:', square(5), cube(2))
	print('fib(10):', fib(10))

	@my_decorator
	def greet(name):
		return f'hello {name}'

	print(greet('world'))

	a = Person('Alice', 30)
	b = Person('Bob', 25)
	print('comparison:', a > b, a == b)

	print(fun(10), fun('abc'), fun(3.14))

	lst = [3, 1, 2]
	lst.sort(key=cmp_to_key(cmp))
	print('sorted with cmp_to_key:', lst)

	d = Data(10)
	print('cached_property first:', d.expensive)
	print('cached_property second (cached):', d.expensive)
