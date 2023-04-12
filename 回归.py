def merge(left_lis, right_lis):
    left_loc = 0  # 左边有序数组的起始位置
    right_loc = 0  # 右边有序数组的起始位置

    result = []  # 每次接收余下两个数组中的最小值

    while left_loc < len(left_lis) and right_loc < len(right_lis):  # 控制两个指针不越界
        if left_lis[left_loc] < right_lis[right_loc]:  # 如果左边的最小值小于右边的最小值
            result.append(left_lis[left_loc])  # 将最小值放到result中
            left_loc += 1
        else:  # 如果右边的最小值小于左边的最小值
            result.append(right_lis[right_loc])  # 将最小值放到result中
            right_loc += 1

    # todo:跳出循环后，一定有一遍的数组为空了
    mod_left_lis = left_lis[left_loc:]
    mod_right_lis = right_lis[right_loc:]

    result = result + mod_right_lis + mod_left_lis  # 左右一定有一个空数组，所以前后顺序没关系
    print(result)
    return result


def merge_sort(lis):
    """分解-归并"""
    # 第一步： 分解
    if len(lis) <= 1:
        return lis  # 出口
    mid_loc = len(lis) // 2  # 选择中间位置分解
    left_list = merge_sort(lis[:mid_loc])
    right_list = merge_sort(lis[mid_loc:])
    # 第二步： 归并
    return merge(left_list, right_list)


if __name__ == '__main__':
    lis = [10, 4, 6, 3, 8, 2, 5, 7]
    print(f"排序前：{lis}")
    new_lis = merge_sort(lis)
    print(f"排序后：{new_lis}")