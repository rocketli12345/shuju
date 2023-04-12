def sift(data, last_f, end_loc):
    """
    一次调整，构造成大根堆
    :param data: 需要构造的树
    :param last_f: 父节点
    :param end_loc: data的最后一个元素索引
    :return:
    """
    i = last_f  # 领导位置
    j = 2 * i + 1  # 领导的左膀，j+1是右臂
    tmp = data[i]  # 需要调整的领导 的能力（值）
    while j <= end_loc:
        # 判断左膀右臂中最高的能力者是左膀/右臂
        if j < end_loc and data[j] < data[j + 1]:  # 如果右臂存在，且能力值强于左臂
            j = j + 1  # j表示可能要取代领导的位置
        # 判断左膀右臂中最高的能力者是不是比领导高,比领导高则取代领导的位置
        if tmp < data[j]:  # 领导能力不够,换领导
            data[i] = data[j]  # j位置（能力强的下属位置）坐上领导的位置，
            i = j  # j位置（能力强的下属位置）暂时给领导，但是不是直接让领导接手
            j = 2 * i + 1  # j位置（能力强的下属位置）的左膀，老领导想要做这个位置，还得看原来下属的下属服不服
        else:  # 领导能力够，那就不变动
            break
    # todo；如果代码运行到这里，则i就是领导最后应该待的位置
    data[i] = tmp


def heap_sort(lis):
    # 第一步： 构造堆
    n = len(lis)
    for i in range(n // 2 - 1, -1, -1):  # 最后一个元素的父节点是 n//2-1
        sift(lis, i, n - 1)
    print("构造大根堆后：",lis)
    # 第二步：出数： 堆顶元素（市长退休）  第三步： 重复第二步
    for j in range(n - 1, -1, -1):
        # lis[0]就是大根堆的堆顶 j就是最后的元素位置
        lis[j], lis[0] = lis[0], lis[j]
        print("出数后（领导不称职）：", lis)
        # 临时的市长lis[j]是 最后元素替换上来的，不称职
        sift(lis, 0, j - 1)  # 堆除了根节点，其他都满足大根堆，所以last_f=0
        print("调整后（领导称职）：", lis)


lis = [9, 8, 7, 6, 5, 2, 4, 3]
heap_sort(lis)
print(lis)
