# 内置模块、第三方模块，自定义模块
# 导入模块
import math
print(math.sqrt(16))
# 导入多个模块
import random, os
print(random.randint(1, 10))
print(os.getcwd())

# 导入模块中的内容
from math import sqrt
print(sqrt(16))

#from math import *
# 到入模块中的多个内容，并取别名
from math import sqrt as s
print(s(16))


# 内容全局变量__name__，用来控制py文件在不同的场景执行不同的逻辑
#文件被当做模块导入时，__name=="__main__"下的代码不会被显示出来

# import 导入包时，首先执行__init__.py文件
# __all__ 本质上是一个列表，用来控制导入的模块
