class SingleCirNode():
    """
    单项链接点
    """
    def __init__(self, item):
        self.item = item  # 储放元素
        self.next = None  # 链接域，存放下一个节点的标识


class SingleCirList():
    def __init__(self):
        self.__head = None