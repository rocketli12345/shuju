def insert_sort():
     n = len(list)
     for i in range(1, n):
         tamp = list[i]  # 抽出来的牌
         j = i - 1
         while j >= 0 and list[j] > tamp:  # 查询数据list[i]前一个数据是否大于他
             list[j + 1], list[j] = list[j], list[j + 1]
             j = j - 1


if __name__ == '__main__':
    list = [2, 3, 4, 1, 9, 6, 8, 7, 5]
    print('运行程序前:', list)
    insert_sort()
    print('运行程序后:', list)