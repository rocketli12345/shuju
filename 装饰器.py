import time
import random


def outer(func):
    def inner(*args, **kwargs):
        start_time = time.time()  # 开始时间
        func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}耗时：{end_time - start_time}秒")

    return inner
# def outer(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()  # 开始时间
#         func(*args, **kwargs)
#         end_time = time.time()  # 结束时间
#         print(f"{func.__name__}耗时：{end_time - start_time}秒")
#
#     return inner

@outer
def insert_sort(lis):
    n = len(lis)
    for i in range(1, n):
        tamp = lis[i]  # 抽出来的牌
        j = i - 1
        while j >= 0 and lis[j] > tamp:  # 查询数据list[i]前一个数据是否大于他
            lis[j + 1], lis[j] = lis[j], lis[j + 1]
            j = j - 1


if __name__ == '__main__':
    lis = [random.randint(0,1000) for i in range(1000)]
    insert_sort(lis)