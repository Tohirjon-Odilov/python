class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = newNode

    def pop(self):
       if self.head is None:
           print('Stack is empty')
       elif self.head.next is None:
            self.head = None
       else:
            cur_node = self.head
            while cur_node.next is not None:
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = None

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next



n1 = Node('Print')
n2 = Node('List')
n3 = Node('Map')
n4 = Node('Lst')

s = Stack()
s.push(n1)
s.push(n2)
s.pop()
s.push(n3)
s.push(n4)
s.printList()