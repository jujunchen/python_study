# if判断
a = 11 
if a > 10: 
    print('a大于10')

a = None
if not a:
    print('a 为 None，在条件判断中被视为 False')

b = []
if not b:
    print('空列表 b 在条件判断中被视为 False')

c = ''
if not c:
    print('空字符串 c 在条件判断中被视为 False')    