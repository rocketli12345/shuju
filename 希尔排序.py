def insert_sort1(lis):
    n = len(lis)

    gap = n // 2  # 取整
    while gap >= 1:
        for i in range(gap, n):
            j = i
            while j >= gap and lis[j - gap] > lis[j]:
                lis[j - gap], lis[j] = lis[j], lis[j - gap]
                j -= gap
        print(f'gap为{gap}的lis{lis}')
        gap = gap // 2


if __name__ == '__main__':
    lis = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    print(f'排列前的lis{lis}')
    insert_sort1(lis)
    print(f'排列后的lis{lis}')
