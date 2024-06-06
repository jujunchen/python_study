# 元组格式 tua = (1,2,3)
tua = (1,2,3)
print(tua)

# 只有一个元素的时候，末尾要加,否则返回唯一值的数据类型
tua = (1,)
print(tua)

# 元组只支持查询，不支持增删改
# count、index、len 等跟列表一样
print(tua.count(1))