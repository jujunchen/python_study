"""
group: None = None, c , 组,目前只能是None
target: ((...) -> object) | None = None, 目标函数
name: str | None = None, 进程名
args: Iterable[Any] = (), 参数
kwargs: Mapping[str, Any] = {}, 关键字参数
*,
daemon: bool | None = None, 是否是守护进程 
"""

# import multiprocessing
# import os
# import time

# def worker(name):
#     """模拟一个进程执行的任务"""
#     print(f"进程 {name},id: {os.getpid()} 开始执行")
#     time.sleep(2)  # 模拟耗时操作
#     print(f"进程 {name} 执行结束")

# if __name__ == "__main__":
#     # 创建进程对象
#     process = multiprocessing.Process(target=worker, args=("Worker-1",))

#     # 启动进程
#     process.start()

#     # 等待进程完成
#     process.join()

#     print("所有进程执行完毕")


# 进程不共享全局变量，测试    
import multiprocessing

list1  = []

def add_list():
    for i in range(10):
        list1.append(i)
    print(f"完成添加数据{list1}")

def read_list():
    print(f"读取的数据{list1}")

if __name__ == "__main__":
    # 创建进程对象
    process1 = multiprocessing.Process(target=add_list)
    process2 = multiprocessing.Process(target=read_list)
    process1.start()
    # 等待添加结束
    process1.join()
    process2.start()
    # 主进程读取全局变量
    print(f"主进程读取的数据{list1}")
 