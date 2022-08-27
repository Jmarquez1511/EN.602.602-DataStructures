class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __le__(self, other) -> bool:
        return self.data <= other.data

    def __lt__ (self, other) -> bool:
        return self.data < other.data

    def walk_list(self):
        print(self.data)
        temp = self.next
        while temp:
            print(temp.data)
            temp = temp.next

    def make_list(self):
        list_ = []
        list_.append(self.data)
        temp = self.next
        while temp:
            list_.append(temp.data)
            temp = temp.next
        return list_


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is None and not found:
            if current.get_data() == item:
                found = True
        else:
            current = current.get_next()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def copy_list(head):
    """
    from https://www.techiedelight.com/clone-given-linked-list/
    :param head:
    :return:
    """
    current = head  # used to iterate over the original list
    newList = None  # head of the new list
    tail = None  # point to the last node in a new list

    while current:
        # special case for the first new node
        if newList is None:
            newList = Node(current.data)
            tail = newList
        else:
            tail.next = Node()
            tail = tail.next
            tail.data = current.data
            tail.next = None
        current = current.next

    return newList

