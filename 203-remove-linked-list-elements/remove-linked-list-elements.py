# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:

        if head == None:
            return None

        temp = head

        while temp.next != None:
            if  temp.next.val == val :
                temp.next = temp.next.next
            else:
                temp = temp.next
        if head != None and head.val == val:
            head = head.next

        return head
        