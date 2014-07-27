class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x

    def insert(self, x):
        if x < self.data:
            if self.left:
                self.left.insert(x)
            else:
                self.left = Node(x)
        elif x > self.data:
            if self.right:
                self.right.insert(x)
            else:
                self.right = Node(x)

    def lookUp(self, x, parent = None):
        if x < self.data:
            if self.left:
                return self.left.lookUp(x, self)
            else:
                return None, None
        elif x > self.data:
            if self.right:
                return self.right.lookUp(x, self)
            else:
                return None, None
        else:
            return self, parent

    def childrenCount(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def delete(self, x):
        node, parent = self.lookUp(x)
        if node:
            childrenCnt = node.childrenCount()
            if childrenCnt == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif childrenCnt == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                del node
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compareTree(self, node):
        if node is None:
            return False
        if self.data != node.data:
            return False

        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compareTree(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compareTree(node.right)
        return res

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data,)
        if self.right:
            self.right.printTree()

    def treeData(self):
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right

if __name__ == '__main__':
    root = Node(8)
    nodeList = [3,10,1,6,4,7,14,13]
    for n in nodeList:
        root.insert(n)
    node, parent = root.lookUp(4)
    print(node.data, parent.data)
    root.delete(3)
    print(root.printTree())
    for d in root.treeData():
        print(d)