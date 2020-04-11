# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        temp = head
        temp2 = head
        while temp2 != None and temp2.next != None:
            temp = temp.next
            temp2 = temp2.next.next
        return temp
        