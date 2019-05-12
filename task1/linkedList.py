class Node(object):
  """docstring for Node"""
    def __init__(self, e=0):
        super(Node, self).__init__()
        self.element = e
        self.next = None

class biNode(Node):
    """docstring for biNode"""
    def __init__(self, e=0):
        super(biNode, self).__init__(e)
        self.before = None
        

class linkedList(object):
    """docstring for linkedList"""
    def __init__(self):
        super(linkedList, self).__init__()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.size = 0


    def insert(self, e):
        n = self.head
        while n.next != self.tail:
            n = n.next
        new_node = Node(e)
        n.next = new_node
        new_node.next = self.tail
        self.size += 1

    def remove(self, e):
        n = self.head
        while n.next != self.tail:
            if n.next.element = e:
                n.next = n.next.next
                self.size -= 1
                return
            else:
                n = n.next
        raise Exception('failed for e not in list')

class biLinkedList(linkedList):
    """docstring for biLinkedList"""
    def __init__(self):
        super(biLinkedList, self).__init__()
        self.head = biNode()
        self.tail = biNode()
        self.head.next = self.tail
        self.tail.before = self.head

    def insert(self, e):
        before_n = self.tail.before
        n = biNode(e)
        self.tail.before = n
        n.before = before_n
        n.after = self.tail
        before_n.next = n

    def remove(self, e):
        n = self.head
        while n.next != self.tail:
            if n.next.element = e:
                n.next.next.before = n
                n.next = n.next.next
                self.size -= 1
                return
            else:
                n = n.next
        raise Exception('failed for e not in list')

class recurentList(linkedList):
    """docstring for recurent"""
    def __init__(self):
        super(recurentList, self).__init__()
        self.head.next = self.head
        delete(self.tail)

    def insert(self, e):
        n = self.head
        while n.next != self.head:
            n = n.next
        new_node = Node(e)
        n.next = new_node
        new_node.next = self.head
        self.size += 1

    def remove(self, e):
        n = self.head
        while n.next != self.head:
            if n.next.element = e:
                n.next = n.next.next
                self.size -= 1
                return
            else:
                n = n.next
        raise Exception('failed for e not in list')

def reversal(ll):
    pre_n = ll.head
    n = pre_n.next
    aft_n = n.next

    while aft_n != None:
        n.next = pre_n
        pre_n = n
        n = aft_n
        aft_n = n.next

    return ll

def getMidNode(ll):
    slow = ll.head
    fast = ll.head
    while fast != ll.tail and fast != None:
        slow = slow.next
        fast = fast.next.next

    return slow