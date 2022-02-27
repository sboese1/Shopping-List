class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_to_end(self, node):
        if linked.head is None:
            linked.head = node
            return

        final = linked.head
        while final.next is not None:
            final = final.next

        final.next = node


    def print_list(self):
        temp = linked.head

        while temp is not None:
            print(temp.data)
            temp = temp.next



linked = linked_list()

title = input("What is the name of your shopping list? ")
answer = 'Y'

while answer.upper() == 'Y':
    item = input("Enter the name of the item to put on the list: ")
    n = Node(item)
    linked.add_to_end(n)
    answer = input("Do you want to enter another item? ")


linked.print_list()
