import threading
import time
import queue

counter = 0
counter_lock = threading.Lock()
counter_rlock = threading.RLock()
counter_sem = threading.Semaphore(1)
task_queue = queue.Queue()


def worker(name, delay):
    """工作线程示例函数，使用锁保证线程安全"""
    global counter
    for i in range(3):
        with counter_lock:
            counter += 1
            current = counter
        print(f"线程 {name} 第{i + 1}次运行, 计数器={current}")
        time.sleep(delay)
    print(f"线程 {name} 完成")

def worker2(name, delay):
    """工作线程示例函数，使用锁保证线程安全"""
    global counter
    for i in range(3):
        with counter_lock:
            counter += 1
            current = counter
        print(f"线程 {name} 第{i + 1}次运行, 计数器={current}")
        time.sleep(delay)
    print(f"线程 {name} 完成")    


def worker_with_rlock(name, delay):
    """使用可重入锁的线程安全计数器示例"""
    global counter
    for i in range(3):
        with counter_rlock:
            counter += 1
            current = counter
        print(f"线程 {name} RLock 第{i + 1}次运行, 计数器={current}")
        time.sleep(delay)
    print(f"线程 {name} 完成(RLock)")


def worker_with_semaphore(name, delay):
    """使用信号量保证线程安全的计数器示例"""
    global counter
    for i in range(3):
        # 使用二进制信号量（值为1）作为互斥锁，或者把初始值设为>1以限制并发数
        with counter_sem:
            counter += 1
            current = counter
        print(f"线程 {name} Semaphore 第{i + 1}次运行, 计数器={current}")
        time.sleep(delay)
    print(f"线程 {name} 完成(Semaphore)")


def producer():
    """生产者线程，向线程安全队列添加任务"""
    for item in range(1, 4):
        task_queue.put(item)
        print("生产者已添加任务", item)
        time.sleep(0.5)
    task_queue.put(None)
    task_queue.put(None)


def consumer(name):
    """消费者线程，从线程安全队列中获取任务"""
    while True:
        item = task_queue.get()
        if item is None:
            task_queue.task_done()
            break
        print(f"线程 {name} 处理任务 {item}")
        time.sleep(1)
        task_queue.task_done()
    print(f"线程 {name} 消费完成")


def main():
    # 创建两个线程，使用 Lock 示例线程安全计数器
    thread1 = threading.Thread(target=worker, args=("A", 1))
    thread2 = threading.Thread(target=worker2, args=("B", 1.5))

    # 使用 RLock 作为另一种锁示例
    thread3 = threading.Thread(target=worker_with_rlock, args=("C", 0.8))
    # 使用 Semaphore 示例
    thread4 = threading.Thread(target=worker_with_semaphore, args=("F", 0.6))

    # 生产者-消费者示例，使用 Queue 保证线程安全
    producer_thread = threading.Thread(target=producer)
    consumer1 = threading.Thread(target=consumer, args=("D",))
    consumer2 = threading.Thread(target=consumer, args=("E",))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    producer_thread.start()
    consumer1.start()
    consumer2.start()

    # 主线程等待子线程结束
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    producer_thread.join()
    task_queue.join()
    consumer1.join()
    consumer2.join()

    print("所有线程已完成, 最终计数器:", counter)


if __name__ == "__main__":
    main()

