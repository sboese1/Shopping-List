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


    def remove_from_end(self):
        if linked.head is None:
            return

        final = linked.head
        while final.next.next is not None:
            final = final.next

        final.next = None


    def remove_specific(self, item):
        if linked.head is None:
            return

        if linked.head.next is None:
            linked.head = None
            return

        current = linked.head.next
        prev = linked.head
        while current.next is not None:
            if str(current.data) == item:
                prev.next = current.next
                return

            current = current.next
            prev = prev.next


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
    while answer.upper() != 'Y' and answer.upper() != 'N':
        answer = input("Invalid input. Please input Y/N: ")


remove = input("Do you want to remove an item? ")
while remove.upper() == 'Y':
    option = input("Do you want to remove the last item or a specific item? (L/S) ")
    while option.upper() != 'L' and option.upper() != 'S':
        option = input("Invalid input. Please input L/S: ")

    if option.upper() == 'L':
        linked.remove_from_end()
    else:
        spot = input("What item do you want to remove? ")
        linked.remove_specific(spot)

    remove = input("Do you want to remove an item? ")


linked.print_list()
