class node(object):
    def __init__(self, x = None, nextNode = None):
        self.data = x
        self.next = nextNode

    def __str__(self):
        return str(self.data)

    def printList(self, node):
        while node:
            print(node)
            node = node.next

    def printBackward(self, node):
        if node is None:
            return
        else:
            current = node
            node = node.next
            self.printBackward(node)
            print(current)


if __name__ == '__main__':
    main()
