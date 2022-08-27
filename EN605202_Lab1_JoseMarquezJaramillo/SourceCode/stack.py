class Stack:
    """
    This class implements a Stack using common list methods from the python language. No input is required, It generates
    a Stack object. The implementation follows closely the Miller and Ranum implementation in listing 3.1. This stack
    implementation is based on the use of a built-in list class from Python, making also use of some built in
    methods as list.pop()
    """

    def __init__(self):
        """
        Initialize
        """
        self.items = []

    def is_empty(self):
        """
        Check if stack is empty, return boolean
        :return: bool
        """
        return self.items == []

    def push(self, item):
        """
        Push item into stack
        :param item:
        """
        self.items.append(item)

    def pop(self):
        """
        pop last item from stack using the built-in list method
        :return: self
        """
        return self.items.pop()

    def peek(self):
        """
        Retrieve the head of the stack, do not modidy the stack
        :return: item
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
        Return the size of the stack
        :return: int
        """
        return len(self.items)

    def __str__(self):
        """
        Operator overload for print method
        :return:
        """
        return ''.join(self.items)
