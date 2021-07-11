import pdb
from list import Node, LList

__list1 = LList()
__list2 = LList()
__answer_list = LList()

def take_input(msg):
    print(msg)
    input_list = input("enter space separated values, ")
    return [int(i) for i in input_list.split(' ')]


def main():
    list1 = take_input("Insert elements for List1")
    for i in list1:
        __list1.insert(i)

    list2 = take_input("Insert elements for List2")
    for i in list2:
        __list2.insert(i)

    list_head = list_addition(__list1.head, __list2.head, 0)
    while list_head:
        print("% s -> " % [list_head.value], end = ' ')
        list_head = list_head.next


def list_addition(node1, node2, quo):
    pdb.set_trace()
    if not (node1 or node2):
        if quo != 0:
            return Node(quo)
        else:
            return None

    node1_value = node1.value if node1 else 0
    node2_value = node2.value if node2 else 0

    pdb.set_trace()
    addition = node1_value + node2_value + quo
    value = addition % 10
    quotient = int((addition - value)/10)

    pdb.set_trace()
    next_node1 = node1.next if node1 else None
    next_node2 = node2.next if node2 else None

    node = list_addition(next_node1, next_node2, quotient)
    pdb.set_trace()
    return Node(value, node)
