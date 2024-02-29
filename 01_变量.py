'''
1. 见名知义
2. 下划线分割法：多个单词组成的名称，使用小写字母，单词与单词之间使用下划线分开
3. 大驼峰命名法： 多个单词组成的名称，每个单词的首字母大写，其余小写
4. 小驼峰命名法： 多个单词组成的名称，第一个单词的首字母小写，其余单词的首字母大写
'''

# 变量名 = 值
a = 1
b = 2
# 保存和
c = a + b
print(c)

# 数值类型
# 整数
num = -5
# 检测数据类型的方法
print(type(num))
# float类型
num2 = 3.14
print(type(num2))
# 布尔型,首字母必须大写
bool = True
print(type(bool))
# complex 复数型，a是实部，b是虚部，j是虚部单位 c = a + bj
c = 1 + 2j
print(type(c))

# 字符串
# 特点：单引号，双引号都行，包含了多行内容的时候可以使用三引号
str = 'hello world'

# 格式化输出
# % 占位符
name = '张三'
print('你好，%s' % name)
# %d 整数
age = 18
print("我的名字是%s,今年%d岁" % (name, age))
# %4d 整数，占4位空白
print("%4d" % age)
# %04d 整数，占4位，左边用0填充
print("%04d" % age)
# %.4f 浮点数
a = 3.1415926
print("%f" % a) # 默认保留小数点后6位，四舍五入
print("%.4f" % a)
# %%
print("我是%%的1%%" % ())
print("我是%")

# f格式化，f{表达式}
print(f"我是{name}，今年{age}岁")