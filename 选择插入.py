def selection_sort():
    n = len(list1)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if list1[min] > list1[j]:
                min = j
                list1[min], list1[i] = list1[i], list1[min]
        print(f"第{i+1}次查找，{list1}")


if __name__ == '__main__':
    list1 =[22,67,34,23,97,89,56,13,71]
    print('运行程序前:', list1)
    selection_sort()
    print('运行程序后:', list1)