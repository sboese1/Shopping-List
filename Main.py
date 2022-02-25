class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None


def add_to_end(node):
    if ll.head.data != None:
        ll.head.next = node
    else:
        ll.head = node


ll = linked_list()
ll.head = Node()


title = input("What is the name of your shopping list? ")
answer = 'Y'

while answer.upper() == 'Y':
    item = input("Enter the name of the item to put on the list: ")
    n = Node(item)
    add_to_end(n)
    answer = input("Do you want to enter another item? ")


while ll.head != None:
    print(ll.head.data)
    ll.head = ll.head.next
