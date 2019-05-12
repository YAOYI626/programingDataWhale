def creat_array_as_len(size, init_element=0):
    l = list()
    for _ in range(size):
        l.append(init_element)
    return l


# 1
class dynamicArray(object):
  """docstring for Array"""
    def __init__(self, init_size):
        super(dynamicArray, self).__init__()
        self.init_size = init_size
        self.max_size = init_size
        self.elements = creat_array_as_len(init_size)
        self.size = 0

    def __expand__(self):
        expand = creat_array_as_len(self.size)
        self.elements += expand
        self.max_size *= 2

    def insert(self, e):
        self.size += 1
        if self.size > self.max_size:
            self.__expand__()
        self.elements.append(e)


# 2
class dynamicArray(object):
    """docstring for Array"""
    def __init__(self, max_size):
        super(dynamicArray, self).__init__()
        self.max_size = max_size
        self.size = 0
        self.elements = creat_array_as_len(max_size)

    def insert(self, e):
        if self.size == self.max_size:
            raise Exception('failed for not enough capacity') 
        self.size += 1
        self.elements.append(e)

    def remove(self, e):
        self.elements.remove(e)
        if self.size == len(self.elements):
            raise Exception('failed for the input not in the array')
        else:
            self.size -= 1

    def alter(self, index, e):
        if index < 0 or index > self.size:
            raise Exception('failed for the invalid index')
        self.elements[index] = e

# 3
def merge(l1, l2):
    l = creat_array_as_len(len(l1)+len(l2))
    i = 0
    while i < min(len(l1), len(l2)):
        if l1[0] < l2[0]:
            l.append(l1[0])
            l1.pop(0)
        else:
            l.append(l2[0])
            l2.pop(0)
        i += 1

    if len(l1) != 0:
        l += l1
    else:
        l += l2

    return l
