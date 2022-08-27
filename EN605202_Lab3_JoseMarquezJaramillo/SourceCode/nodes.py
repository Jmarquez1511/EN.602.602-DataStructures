class LeafNode:
    """
    has None type left and right children
    """
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left  = None
        self.right = None

    def printtree(self):
        print(self)

    def __str__(self):
        return str(self.character)+','+str(self.frequency)


class InternalNode:
    def __init__(self, frequency, left, right):
        self.frequency = frequency
        self.left = left
        self.right = right
        self.character = None

    def __str__(self):
        return str(self.character)+','+str(self.frequency)

