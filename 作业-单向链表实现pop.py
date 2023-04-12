class SingleNode():
    """单向链表节点"""

    def __init__(self, item):
        self.item = item  # 存放数据元素
        self.next = None  # 链接域，存放下一个节点的标识


class SingleLinkList():
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
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        """头部添加元素"""
        #将item变成一个节点
        node = SingleNode(item)
        #将呆插入的节点的next指向原来的头结点
        node.next = self.__head
        #self.__head指向当前节点
        self.__head = node


    def append(self,item):
        """尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            #第一步：找到尾节点，注意不是尾结点的链接域
            while cur.next != None:
                cur = cur.next
            #第二步：尾结点的链接域指向新节点
            cur.next = node

    def insert(self,pos,item):
        """指定位置插入元素"""
        if pos<=0:
            self.add(item) #位置小于0就头插入
        elif pos > self.length()-1: #位置大于长度减1就尾插入
            self.append(item)
        else:
            #item生成节点
            node = SingleNode(item)
            #要插入的位置的节点的前一个节点pre,pre.next就是要插入位置的节点，将变成新节点的下一节点
            pre = self.__head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            #新节点指向位置原来的节点
            node.next = pre.next
            #位置原来的节点的前一个节点指向新节点
            pre.next = node

    def pop(self,pos):
        """删除指定位置"""
        pre = None  #前节点
        cur = self.__head
        if pos <= 0:
            self.__head = cur.next # 位置小于0就头插入
        else:
            # 位置的节点的前一个节点pre,pre.next就是位置下一节点cur.next
            count = 0
            while count < pos - 1:
                count += 1
                pre = cur
                cur = cur.next
            pre.next = cur.next

    def remove(self,value):
        """删除值为value的节点"""
        pre = None  #前节点
        cur = self.__head
        while cur != None: #遍历所有节点，如果找到节点则删除并退出
            if cur.item == value: #找到了节点
                if pre == None: #如果删除的是头结点
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break #只要找到删除后，跳出循环
            else: #没有找到，链接域移向下一个节点
                pre = cur
                cur = cur.next

    def search(self,value):
        cur = self.__head
        while cur != None: #遍历所有节点，如果找到节点则删除并退出
            if cur.item == value: #找到了节点
                return True
            else: #没有找到，链接域移向下一个节点
                cur = cur.next
        return False


l = SingleLinkList()

l.add(0)
l.add(1)
l.add(2)
l.append(4)
l.append(5)
l.insert(3,"哈哈")
l.remove(2)
l.travel()
print(l.search("哈哈哈"))
print(l.search("哈哈"))





