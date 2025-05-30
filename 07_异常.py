# 异常捕获
# try:
#     print(a)
# except:
#     print("异常")


try:
    print(a)
except Exception as e:
    print("变量未定义", e)


# 没有异常时候执行的代码
try:
    print(a)
except Exception as e:
    print("变量未定义", e)
else:
    print("没有异常")

# 无论是否检测到异常，都会执行的代码
try:
    print(a)
except Exception as e:
    print("变量未定义", e)
else:
    print("没有异常")
finally:
    print("不管有没有异常都会执行的代码")


# 抛出异常
try:
    print(a)
except Exception as e:
    # print("变量未定义", e)
    raise Exception("变量未定义")