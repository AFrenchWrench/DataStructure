class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{str(self.prev)} -> {str(self)} -> {str(self.next)}"


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def merge(self, node, nums):
        end = node.next
        for n in nums:
            prev = node
            node.next = Node(n)
            node = node.next
            node.prev = prev
        node.next = end
        end.prev = node

        return node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        return node.prev

    def __repr__(self):
        s = ""
        node = self.head
        while node:
            s += str(node.data) + " "
            node = node.next
        return s


n = int(input())
ll = LinkedList()
cursor = ll.head


for _ in range(n):
    command = input()
    if command == "merge":
        n = int(input())
        nums = list(map(int, input().split()))
        cursor = ll.merge(cursor, nums)
    elif command == "prev":
        cursor = cursor.prev
    elif command == "next":
        cursor = cursor.next
    elif command == "remove":
        cursor = ll.remove(cursor)
    elif command == "print":
        if cursor:
            print(cursor.data if cursor.data is not None else "null")
        else:
            print("null")
