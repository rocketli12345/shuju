def bubble_sort():
    n = len(list)
    for i in range(n-1):  # 代表循环几次
        exchange = False  # 代表数据没有更替了
        for j in range(n-1-i):  # 修改 查找数据
            if list[j] > list[j+1]:  # 如果前面数据大于后面数据则后移
                tap = list[j]
                list[j] = list[j+1]  # 替换
                list[j+1] = tap
                exchange = True
        if exchange == False:
            break
        print(f'数据第{i+1}循环,{list}')


if __name__ == '__main__':
    list = [2, 3, 4, 1, 9, 6, 8, 7, 5]
    print('运行程序前:', list)
    bubble_sort()
    print('运行程序后:', list)