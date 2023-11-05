class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Link_list:
    def __init__(self) -> None:
        self.head = None
        
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = newNode
    
    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def push(self, new_data):
        new_node = Node(new_data)        
        new_node.next = self.head        
        self.head = new_node

    def insertAfter(self,prev_node, new_data):
        if prev_node is None:
            print("this node does not exist")    
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node 
        
    def delete(self, data):
        cur_node = self.head
        
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return
        
        while cur_node:
            if cur_node.data == data:
                break
            prev = cur_node
            cur_node = cur_node.next
            
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None
         

    def lens(self):
        len = 0
        cur_node = self.head
        while cur_node:
            len+=1
            cur_node = cur_node.next
        return len
    
    def appendList(self):
        nums = list()
        cur_node = self.head
        while cur_node:
            nums.append(cur_node.data)
            cur_node = cur_node.next
        return nums


n1 = Node(10)
n2 = Node(15)
n3 = Node(5)
n4 = Node(20)

l1 = Link_list()
l1.insert(n1)
l1.insert(n2)
l1.insert(n3)
l1.insert(n4)

    
l1.printList()