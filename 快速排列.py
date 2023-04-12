def fast_sort(l_sort, r_sort):
    tamp = list[l_sort]
    while l_sort < r_sort:
        while list[r_sort] > tamp and l_sort < r_sort:  # 右边数据跟拉出来的数据对比得出
            r_sort -= 1
        # 跳出循环
        list[l_sort] = list[r_sort]
        while list[l_sort] < tamp and l_sort < r_sort:   # 左边边数据跟拉出来的数据对比得出
            l_sort += 1
        # 跳出循环
        list[r_sort] = list[l_sort]
    list[r_sort] = tamp
    return r_sort


def quick_sort(l_sort, r_sort):
    if l_sort < r_sort:
        mid = fast_sort(l_sort, r_sort)
        quick_sort(l_sort, mid)  # 调用自己
        quick_sort(mid, l_sort)


if __name__ == '__main__':
    list = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    # print(f'排列前的数据{list}')
    # l_sort = 0
    # r_sort = len(list) - 1
    # fast_sort(l_sort, r_sort)
    # print(f'排列后的数据{list}')

    print(f'排列前的数据{list}')
    quick_sort(0, len(list) - 1)
    print(f'排列后的数据{list}')
