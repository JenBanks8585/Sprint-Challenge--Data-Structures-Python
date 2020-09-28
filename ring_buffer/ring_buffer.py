class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]

    def append(self, item):
        self.storage.pop(0)
        self.storage.append(item)
    
    def get(self):
        return [i for i in self.storage if i is not None]

    def length(self):
        return self.storage.__len__()



A = RingBuffer(5)
A.append(1)
A.append(2)
A.append(3)
A.append(4)
A.append(5)
A.append(6)
#for i in range(49):
#    A.append(i)
#A.append('a')
#A.append('b')
#A.append('c')
#A.append('d')
#A.append('e')
#A.append('f')
#
#A.append('a')
#A.append('b')
#A.append('c')
#A.append('d')
#A.append('e')
#A.append('f')
#A.append('g')
#A.append('h')
#A.append('i')
print(A.length())
print(A.get())