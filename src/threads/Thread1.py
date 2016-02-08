# Thread1.py


import threading
import time
import random


class jdThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
        self.create_time = time.time()
        self.local = threading.local()

    def run(self):
        self.local = []
        time.sleep(1)
        print("线程", self.num, "被创建")

        for i in range(8):
            self.local.append(random.randrange(10))
        print(threading.currentThread(), self.local)

        print(time.time() - self.create_time)

        print("线程", self.num, "结束")
        print("\n")


print("主线程开始")
for item in range(7):
    t = jdThread(item)
    t.start()
    # join函数控制线程执行顺序，不要在start之前调用join函数
    # t.join()
    # isDaemon函数查看线程后台运行状态
    # print(t.isDaemon())
print("主线程结束")
