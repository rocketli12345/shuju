class SingleCycleNode():
    """单向循环链表节点"""

    def __init__(self, item):
        self.item = item  # 存放数据元素
        self.next = None  # 链接域，存放下一个节点的标识


class SingleLinkCycleList():
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        if self.__head == None:
            return True
        else:
            return False

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head.next  # 默认从第二个节点开始
        count = 1
        while cur != self.__head:  # todo:单向循环链表的尾节点指向的是头节点
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:  # todo:单向循环链表的尾节点指向的是头节点
            print(cur.item)
            cur = cur.next
        print(cur.item)

    def add(self, item):
        """头部添加元素"""
        # 将item变成一个节点
        node = SingleCycleNode(item)
        # todo；将尾节点指向新的头节点
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 将待插入的节点的next指向原来的头结点
            node.next = self.__head

            # 先要找到尾节点，再把头指向新节点？  todo: 因为尾节点指向是头节点，如果头节点先改，则找不到尾节点位置了
            cur = self.__head
            while cur.next != self.__head:  # todo:单向循环链表的尾节点指向的是头节点
                cur = cur.next
            cur.next = node  # 找到尾节点后，指向新节点
            # self.__head指向当前新节点
            self.__head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleCycleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            # 第一步：找到尾节点，注意不是尾结点的链接域
            while cur.next != self.__head:
                cur = cur.next
            # 第二步：尾结点的链接域指向新节点
            cur.next = node

            # todo: 新节点指向头节点： 单向循环链表的尾节点指向的是头节点
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置插入元素"""
        if pos <= 0:
            self.add(item)  # 位置小于0就头插入
        elif pos > self.length() - 1:  # 位置大于长度减1就尾插入
            self.append(item)
        else:
            # item生成节点
            node = SingleCycleNode(item)
            # 要插入的位置的节点的前一个节点pre,pre.next就是要插入位置的节点，将变成新节点的下一节点
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 新节点指向位置原来的节点
            node.next = pre.next
            # 位置原来的节点的前一个节点指向新节点
            pre.next = node

    def remove_head(self):
        """删除头节点：找到尾巴，让尾巴指向头的下一个节点"""
        if self.length() <= 1: #只有1个元素或者为空，则删除后直接返回空
            return
        tail = self.__head
        # 第一步：找到尾节点，注意不是尾结点的链接域
        while tail.next != self.__head:
            tail = tail.next
        self.__head = self.__head.next  # 赋予新的头
        # 第二步：尾结点的链接域指向新节点
        tail.next = self.__head

    def remove_tail(self):
        """删除尾节点"""
        if self.length() <= 1:  # 只有1个元素或者为空，则删除后直接返回空
            return

        pre = None
        cur = self.__head
        # 第一步：找到尾节点，注意不是尾结点的链接域
        while cur.next != self.__head:
            pre = cur
            cur = cur.next
        pre.next = self.__head #将尾节点的前一个节点（新的尾巴）指向头

    def remove(self, value):
        """删除值为value的节点"""
        if self.is_empty():
            return
        # 1.判断链表中是否有值为value的节点
        pre = None  # 前节点
        cur = self.__head
        while cur.next != self.__head:  # 单向循环链表的尾节点指向的是头节点
            if cur.item == value:  # 表示找到了值为value的节点
                # 执行删除逻辑
                if pre == None:  # 表示删除的是头节点  #todo:将尾节点指向头节点的下一个节点
                    self.remove_head()
                else:  # 删除其他节点
                    pre.next = cur.next
                # 执行完删除逻辑之后，不要忘了退出循环
                return
            else:  # 继续遍历
                pre = cur
                cur = cur.next

        #如果跳出while循环，cur必然指向尾节点
        if cur.item == value: #如果尾节点是要删除的节点
            self.remove_tail()


    def search(self, value):
        """查找链表中是否存在值为value的节点"""
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == value:  # 找到了节点
                return True
            else:
                cur = cur.next
        if cur.item == value: #如果跳出循环，cur必然指向尾节点
            return True
        return False


if __name__ == '__main__':
    l = SingleLinkCycleList()
    l.add(0)
    l.add(1)
    l.add(2)
    l.add(3)
    l.append(4)
    l.append(5)
    l.insert(3, "哈哈")
    l.remove(1)
    l.travel()  # 请问打印的信息是什么？
