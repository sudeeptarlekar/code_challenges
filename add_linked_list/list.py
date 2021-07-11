class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def is_last_node(self):
        return True if self.next == None else False


class LList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return True if self.head == None or self.tail == None else False

    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def remove(self, value):
        current_node = self.head

        if self.is_empty():
            print("List is Empty")
            return

        while current_node:
            if current_node.value == value and current_node == self.head:
                self.head = current_node.next
                current_node.next = None
                break

            if current_node.next.value == value:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next

    def print(self):
        if self.is_empty():
            print("Linked list is empty")
            return

        print("Here is complete Linked List")
        temp = self.head
        while temp != None:
            print("% s ->" % [temp.value], end = ' ')
            temp = temp.next
        print("None")

