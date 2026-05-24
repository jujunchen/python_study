# 元类（metaclass）是用来创建类的“类”。
# 在 Python 中，类本身也是对象，而元类决定了类对象的创建方式。
# 默认情况下，Python 中的类由 type 创建：
# class A: pass  等价于 A = type('A', (), {})

# 元类常见用途：
# 1. 自动注册类到某个容器中
# 2. 校验类属性或方法是否符合规范
# 3. 动态修改类的定义，如自动生成方法、添加属性等

# 一个简单的元类示例：自动注册所有子类
class AutoRegisterMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace)
        if name != 'Base':
            AutoRegisterMeta.registry[name] = cls
        return cls


class Base(metaclass=AutoRegisterMeta):
    pass


class Foo(Base):
    pass


class Bar(Base):
    pass


# 使用场景：
# 1. 插件系统中，元类可以在类定义时把子类自动注册到插件列表中。
# 2. ORM 框架中，元类可以根据类属性自动生成数据库字段映射。
# 3. 接口检查中，元类可以在类创建时验证是否实现了必须的方法。

if __name__ == '__main__':
    print('Registered classes:', AutoRegisterMeta.registry)
    # 输出：Registered classes: {'Foo': <class '__main__.Foo'>, 'Bar': <class '__main__.Bar'>}
