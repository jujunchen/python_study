"""示例：描述符（descriptor）演示。

包含两个描述符：StringDescriptor 和 IntegerDescriptor，用于在属性访问时
进行类型和范围检查。类 Person 演示了如何将描述符作为类属性使用。

运行此脚本将展示正常赋值、类型错误和数值超出范围时的异常。
"""

class StringDescriptor:
    """描述符：只允许字符串值。

    参数:
        name (str): 存储在实例 __dict__ 中的属性名。
    """
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Can't delete attribute {self.name}")


class IntegerDescriptor:
    """描述符：只允许整数值，可选的最小/最大范围检查。"""
    def __init__(self, name, min_value=None, max_value=None):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Can't delete attribute {self.name}")


class Person:
    # 在类定义中声明描述符作为属性
    name = StringDescriptor('name')
    age = IntegerDescriptor('age', min_value=0, max_value=120)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"


if __name__ == '__main__':
    # 示例用法：
    p = Person('Alice', 30)
    print(p)  # 正常输出

    p.name = 'Bob'
    print('Updated name:', p.name)

    # 触发类型错误（期望整数）
    try:
        p.age = 'thirty'
    except TypeError as exc:
        print('Type error:', exc)

    # 触发值错误（范围检查）
    try:
        p.age = -5
    except ValueError as exc:
        print('Value error:', exc)
