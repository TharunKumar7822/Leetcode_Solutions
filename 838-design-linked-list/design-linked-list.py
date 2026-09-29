class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head

        for i in range(index):
            if temp is None:
                return -1
            temp = temp.next

        if temp is None:
            return -1

        return temp.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        newNode = Node(val)

        newNode.next = temp.next
        temp.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(index - 1):
            if temp.next is None:
                return
            temp = temp.next

        if temp.next is None:
            return

        temp.next = temp.next.next