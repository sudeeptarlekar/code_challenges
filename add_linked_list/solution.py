class Node:
    def __init__(self, value = None, next_node = None):
        self.val = value
        self.next = next_node

    def is_last_node(self):
        return True if self.next == None else False

class Solution:
    def addTwoNumbers(self, node1: Node, node2: Node) -> Node:
        answer_node = Node()
        current_node = answer_node
        carry = 0

        while node1 or node2:
            node1_value = node1.val if node1 else 0
            node2_value = node2.val if node2 else 0
            addition = node1_value + node2_value + carry
            carry = int(addition/10)

            current_node.next = Node(addition % 10)
            current_node = current_node.next

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        if carry > 0:
            current_node.next = Node(carry)

        return answer_node.next
