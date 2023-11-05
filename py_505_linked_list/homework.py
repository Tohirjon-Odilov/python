# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        # print(temp)
        # new = None
        while temp:
            # new = "".join(temp)
            print(temp.val)
            temp = temp.next
            # temp.next = None
        # return int(new, 2)
        

v1 = ListNode(1)
v2 = ListNode(0)
v3 = ListNode(1)
Solution().getDecimalValue(v1)
# Solution().getDecimalValue(v2)
# Solution().getDecimalValue(v3)
        