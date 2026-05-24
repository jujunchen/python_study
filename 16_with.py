"""示例：with 语句的多种用法。

运行此文件会演示：
- 基本文件读写
- 自定义上下文管理器（类实现 __enter__/__exit__）
- 使用 contextlib.contextmanager 装饰器
- 同时管理多个上下文
- 使用 contextlib.suppress 忽略指定异常
"""

from contextlib import contextmanager, suppress
import io
import sys


def example_file_usage():
	# 使用 with 自动管理文件关闭
	with open("example.txt", "w", encoding="utf-8") as f:
		f.write("hello with\n")

	with open("example.txt", "r", encoding="utf-8") as f:
		print('file content:', f.read().strip())


class MyCtx:
	"""自定义上下文管理器：在进入/退出时打印信息。"""
	def __enter__(self):
		print('enter MyCtx')
		return self

	def __exit__(self, exc_type, exc, tb):
		print('exit MyCtx', 'exception=' + str(exc) if exc else 'no exception')
		# 不抑制异常：返回 False 或 None
		return False


@contextmanager
def my_ctx_manager(name):
	print(f'enter {name}')
	try:
		yield name
	finally:
		print(f'exit {name}')


def example_multiple_and_suppress():
	# 同时管理多个上下文（文件 + 自定义上下文）
	with MyCtx() as m, my_ctx_manager('cm') as cm_name:
		print('inside with blocks:', m, cm_name)

	# 忽略特定异常
	with suppress(FileNotFoundError):
		open('nonexistent.file')
	print('suppressed FileNotFoundError')


def example_redirect_stdout():
	# 将 stdout 临时重定向到字符串缓冲区
	buf = io.StringIO()
	# 为了兼容性（不使用外部 redirect），手工示范：
	old = sys.stdout
	try:
		sys.stdout = buf
		print('this goes to buffer')
	finally:
		sys.stdout = old
	print('captured:', buf.getvalue().strip())


if __name__ == '__main__':
	example_file_usage()
	example_multiple_and_suppress()
	example_redirect_stdout()
