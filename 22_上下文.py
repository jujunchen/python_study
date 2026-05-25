# Python 上下文管理器示例
# 方法1：类实现 __enter__ / __exit__

class MyContext:
    def __init__(self, resource_name):
        self.resource_name = resource_name

    def __enter__(self):
        print(f"[{self.resource_name}] 进入上下文，做好准备")
        # 返回的对象可以被 as 绑定
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 无论是否发生异常，都会执行清理工作
        print(f"[{self.resource_name}] 退出上下文，释放资源")
        if exc_type:
            print(f"捕获异常: {exc_type.__name__}: {exc_val}")
            # 返回 True 表示已处理异常，否则异常会继续传播
            return False

    def do_work(self):
        print(f"[{self.resource_name}] 正在使用资源")


# 方法2：使用 contextlib.contextmanager 装饰器
from contextlib import contextmanager

@contextmanager
def my_context_manager(resource_name):
    print(f"[{resource_name}] 进入上下文，做好准备")
    try:
        yield resource_name
    finally:
        print(f"[{resource_name}] 退出上下文，释放资源")


if __name__ == '__main__':
    # 使用类实现的上下文管理器
    with MyContext('ClassResource') as ctx:
        ctx.do_work()

    print('-' * 40)

    # 使用 contextlib.contextmanager 的生成器实现
    with my_context_manager('GeneratorResource') as resource:
        print(f"[{resource}] 正在使用资源")

# 原理和实现步骤：
# 1. 类实现方式
#    - 定义 __enter__(): 进入上下文时执行初始化、获取资源等操作，并可返回上下文管理对象或其他值。
#    - 定义 __exit__(exc_type, exc_val, exc_tb)：退出上下文时执行清理、释放资源等操作。
#      如果 __exit__ 返回 True，则会抑制异常；返回 False 或 None，则异常继续传播。
# 2. 生成器装饰器方式
#    - 使用 contextlib.contextmanager 装饰一个生成器函数。
#    - 在 yield 之前编写进入上下文的逻辑。
#    - yield 后编写退出上下文的逻辑（通常放在 finally 块里）。
#    - with 语句会在进入时运行到 yield，并把 yield 的值绑定给 as 部分；
#      退出时会继续执行 finally 块中的清理逻辑。
