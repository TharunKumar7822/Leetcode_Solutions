class Solution:
    def sortList(self, head):
        values = []

        # Store all values
        while head:
            values.append(head.val)
            head = head.next

        # Sort values
        values.sort()

        # Create sorted linked list
        dummy = ListNode(0)
        current = dummy

        for x in values:
            current.next = ListNode(x)
            current = current.next

        return dummy.next