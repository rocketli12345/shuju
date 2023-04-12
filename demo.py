class SingleNode():
    """
    单项链节点
    """
    def __init__(self, item):
        self.item = item  # 存放数据元素
        self.next = None  # 链接域， 存放下一个节点的标识


class SingleLinkList():
    """单链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur 初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向 None,当未到达尾部时
        while cur != None:
            count += 1
            # 将cur 后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        """头部元素"""
        # 创建一个保存 item 的节点
        node = SingleNode(item)
        # 将新节点的链接区域 next 指向头节点， 即__head 指向的位置
        node.next = self.__head
        # 将链表的__head 指向新节点
        self.__head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 判断是否为空, 若为空则将__head 指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空， 则找到尾部， 将尾部节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置插入"""
        # 若指定位置pos为第一个元素之前， 则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部， 则执行尾部插入
        elif pos > self.length()-1:
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre 用来指定位置pos的前一个位置
            pre = self.__head
            while count < pos -1:
                count += 1
                pre = pre.next
            # 先将新节点的 node 的 next 指向插入位置节点(pre.next)
            node.next = pre.next
            # 再将插入位置的前一个节点 pre 的 next 指向新的节点
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            # 找到指定元素
            if cur.item == item:
            # 如果第一个就是删除的节点(not None)
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的 next 指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        '''链表查找节点是否存在，并返回 True 或 False'''
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
            return False


if __name__ == '__main__':
    l = SingleLinkList()
    l.add(0)
    l.add(1)
    l.add(2)
    l.add(3)
    l.append(4)
    l.append(5)
    l.insert(3, "哈哈")
    l.remove(1)
    l.travel()  # 请问打印的信息是什么？
