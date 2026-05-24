"""
20_装饰器.py

本文件简要解释 Python 中的装饰器，如何创建装饰器，并给出常见应用场景与示例。

装饰器（decorator）是一个高阶函数，它接收一个函数（或可调用对象），并返回一个新的函数。
装饰器常用于在不修改被装饰函数源代码的情况下，添加额外行为（如日志、权限、缓存、计时等）。

示例目录：
 - 基本装饰器
 - 保持函数元数据（functools.wraps）
 - 带参数的装饰器
 - 类装饰器（简单示例）
 - 常见应用场景说明
"""

from functools import wraps
import time
from typing import Callable, Any


# -------------------------------
# 基本装饰器：不带参数
# -------------------------------
def simple_decorator(func: Callable) -> Callable:
	"""一个简单的装饰器：在函数执行前后打印信息并返回原结果。"""

	@wraps(func)
	def wrapper(*args, **kwargs):
		print(f"[DEBUG] calling {func.__name__}")
		result = func(*args, **kwargs)
		print(f"[DEBUG] {func.__name__} returned {result!r}")
		return result

	return wrapper


@simple_decorator
def add(a, b):
	return a + b


# -------------------------------
# 保持函数元数据：functools.wraps
# -------------------------------
# 如果不使用 wraps，wrapper 的 __name__、__doc__ 等会遮蔽原函数，导致调试/文档问题。


# -------------------------------
# 带参数的装饰器（装饰器工厂）
# -------------------------------
def repeat(n: int):
	"""返回一个装饰器，使被装饰函数重复执行 n 次并返回最后一次结果。"""

	def decorator(func: Callable) -> Callable:
		@wraps(func)
		def wrapper(*args, **kwargs):
			result = None
			for i in range(n):
				result = func(*args, **kwargs)
			return result

		return wrapper

	return decorator


@repeat(3)
def greet(name: str):
	print(f"hello {name}")


# -------------------------------
# 计时装饰器（常见用例）
# -------------------------------
def timeit(func: Callable) -> Callable:
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = func(*args, **kwargs)
		end = time.perf_counter()
		print(f"[TIMER] {func.__name__} took {end-start:.6f}s")
		return result

	return wrapper


@timeit
def slow(n: int):
	time.sleep(n)


# -------------------------------
# 缓存装饰器（简单示例）
# -------------------------------
def simple_cache(func: Callable) -> Callable:
	cache = {}

	@wraps(func)
	def wrapper(*args):
		if args in cache:
			return cache[args]
		res = func(*args)
		cache[args] = res
		return res

	return wrapper


@simple_cache
def fib(n: int) -> int:
	if n < 2:
		return n
	return fib(n - 1) + fib(n - 2)


# -------------------------------
# 类装饰器（装饰类或使用类作为装饰器）
# -------------------------------
class CountCalls:
	"""使用类作为装饰器：统计被装饰函数被调用的次数。"""

	def __init__(self, func: Callable):
		wraps(func)(self)
		self.func = func
		self.count = 0

	def __call__(self, *args, **kwargs) -> Any:
		self.count += 1
		print(f"[CALLS] {self.func.__name__} called {self.count} times")
		return self.func(*args, **kwargs)


@CountCalls
def say(msg: str):
	print(msg)


# -------------------------------
# 常见应用场景（总结）
# -------------------------------
# 1. 日志记录（logging）—— 在函数入口/出口记录参数、返回值、异常。
# 2. 权限/鉴权（authorization）—— 在执行前检查用户权限或令牌。
# 3. 缓存（memoization）—— 存储函数结果以避免重复计算（如 lru_cache）。
# 4. 性能监控/计时（profiling/timeit）—— 测量函数耗时、调用频率。
# 5. 重试策略（retry）—— 在异常时重新尝试执行函数。
# 6. 输入验证/类型转换/预处理/后处理。


if __name__ == "__main__":
	print(add(2, 3))      # simple_decorator
	greet("world")       # repeat
	slow(0.1)             # timeit
	print(fib(10))        # simple_cache
	say("first")
	say("second")

