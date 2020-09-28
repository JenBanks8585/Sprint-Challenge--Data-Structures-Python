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

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

        
    def reverse_list(self, node, prev):
        cur = node
        nxt = None
        prev = None
        while cur:
            nxt = cur.next_node
            cur.next_node = prev
            prev = cur
            cur = nxt
            self.head = prev
        return prev

    
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next_node




#B =Node()
A = LinkedList()
#A.add_to_head(1)
#A.add_to_head(2)
#A.add_to_head(3)
#A.add_to_head(4)
#A.add_to_head(5)
#A.add_to_head(6)
#A.add_to_head(7)
for i in range(2,43, 3):
    A.add_to_head(i)
A.print_list()

print('*************')
print("head of linkedlist: ",A.head.get_next().value)

C =  A.reverse_list(A.head, None)

print('*************')
print("head of linkedlist: ",A.head.get_next().value)
print('*************')
print("head of reversed list: ", C.value)
print('*************')
print("2nd node of reversed list: ", C.get_next().value)
print('*************')
print("3rd node of reversed list: ", C.get_next().get_next().value)
print('*************')
print("5th node of reversed list: ", C.get_next().get_next().get_next().get_next().value)
print('*************')

