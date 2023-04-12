class Node:
    def __init__(self,item):
        self.item = item
        self.child1 = None  #左子树
        self.child2 = None  #y右子树

class Tree:
    def __init__(self):
        self.root = None  #根
    def add(self, item):
        """添加元素"""
        # 第一步：将元素变成节点
        node = Node(item)
        #第二步：找到需要插入的位置进行插入
        if self.root is None:  #如果树是空的话
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.child1 is None:
                    pop_node.child1 = node
                    return
                elif pop_node.child2 is None:
                    pop_node.child2 = node
                    return
                else:
                    q.append(pop_node.child1)
                    q.append(pop_node.child2)

    def preorder(self,root):  # 先序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.child1)
        right_item = self.preorder(root.child2)
        return result + left_item + right_item

    def inorder(self,root):  # 中序序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.child1)
        right_item = self.inorder(root.child2)
        return left_item + result + right_item

    def postorder(self,root):  # 后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.child1)
        right_item = self.postorder(root.child2)
        return left_item + right_item + result

    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]  #保存节点的列表
        res = [self.root.item] #保存值的列表
        while q != []:
            pop_node = q.pop(0)
            if pop_node.child1 is not None:
                q.append(pop_node.child1)
                res.append(pop_node.child1.item)

            if pop_node.child2 is not None:
                q.append(pop_node.child2)
                res.append(pop_node.child2.item)
        return res

t = Tree()

for i in "DCABFE":
    t.add(i)

print('层序遍历:',t.traverse())
print('先序遍历:',t.preorder(t.root))
print('中序遍历:',t.inorder(t.root))
print('后序遍历:',t.postorder(t.root))

"""
二叉树的中序遍历是BCFDEA，后续遍历是BFCEAD，前序遍历是？
用python代码展示出来。
DCBFAE
"""