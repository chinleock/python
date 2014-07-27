class Node(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x

class BinaryTree(object):
    def __init__(self):
        self.__init__root = None

    def addNode(self, x):
        return Node(x)

    def insert(self, root, x):
        if root == None:
            return self.addNode(x)
        else:
            if x <= root.data:
                root.left = self.insert(root.left, x)
            else:
                root.right = self.insert(root.right, x)
            return root

    def lookUp(self, root, x):
        if root is None:
            return 0
        else:
            if x == root.data:
                return 1
            else:
                if x < root.data:
                    return self.lookUp(root.left, x)
                else:
                    return self.lookUp(root.right, x)

    def minValue(self, root):
        while(root.left):
            root = root.left
        return root.data

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            return max(leftDepth, rightDepth) + 1

    def size(self, root):
        if root is None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)

    def printTree(self, root):
        if root is None:
            pass
        else:
            self.printTree(root.left)
            print(root.data)
            self.printTree(root.right)

    def printReverseTree(self, root):
        if root is None:
            pass
        else:
            self.printReverseTree(root.right)
            print(root.data)
            self.printReverseTree(root.left)

class NNode(object):
    def __init__(self, x):
        self.data = x
        self.children = []

    def __str__(self):
        return 'Data: {0}; Children:{1}'.format(self.data, self.children)

    def __hash__(self):
        return hash((self.data, self.children))

    __repr__ = __str__

class NTree(object):
    def __init__(self):
        self.root = NNode()

    def getRoot(self):
        return self.root

    def insert(self, node, x):
        if not x:
            pass
        if node and not node.data:
            tmpChild = None
            for child in node.children:
                if x[0] == child.data:
                    tmpChild = child
                    break

            if tmpChild:
                self.insert(x, tmpChild)

            else:
                newNode = NNode(x[0])
                node.children.append(newNode)
                self.insert(x, newNode)
        else:
            if len(x) > 1:
                tmpChild = None
                for child in node.children:
                    if x[1] == child.data:
                        tmpChild = child
                        break
                if tmpChild:
                    self.insert(data[1:], tmpChild)
                else:
                    newNode = NNode(x[1])
                    node.children.append(newNode)
                    self.insert(x[1:], newNode)

    def printTree(self, node):
        container = []
        if node and not node.data:
            print('*Root')
        else:
            container.append('--')
            container.append(node.data)
            print(''.join(container))
            container.pop()
            container.pop()

        if node and node.children:
            container.append('   |')
            print(''.join(container))

        for child in node.children:
            self.printTree(child)

        if node.children and container:
            container.pop()

    def searchTree(self, node, x, path = [], parentNode = None, result = {}):
        if (not x and x.strip()) or not node:
            return False
        if node.data == x:
            path.append(node.data)
            result['parentNode'] = parentNode
            result['node'] = node
            print('Path:{0}'.format('>'.join(path)))
            return True
        else:
            path.append(node.data if node.data else 'Root')
            for child in node.children:
                if self.searchTree(child, x, path, node, result):
                    return True
                else:
                    path.pop()

    def deleteNode(self, x):
        searchContainer = []
        result = {}
        self.searchTree(self.root, x, searchContainer, None, result)
        parentNode = result.get('parentNode')

        for idx in range(len(parentNode.children)):
            if parentNode.children[idx].data == x:
                del parentNode.children[idx]
                break
        return searchContainer[1:]

if __name__ == '__main__':
    naryNode = NNode(18)
    print(naryNode)
