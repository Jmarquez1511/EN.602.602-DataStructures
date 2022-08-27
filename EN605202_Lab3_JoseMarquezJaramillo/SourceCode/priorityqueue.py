from SourceCode.nodes import LeafNode, InternalNode


class PriorityQueue(object):
    def __init__(self):
        """
        initializes a new instances by creating an empty list
        """
        self.queue = []

    def __str__(self):
        """
        operator overloading of the print function, it prints a concatenation of the items in the priority queue.
        """
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isempty(self) -> bool:
        """
        returns a True boolean if the priority queue is empty.
        :return:
        """
        return len(self.queue) == 0


    def enqueue(self, data):
        """
        inserts a new item into the queue. This method preserves the order necessary for Huffman encoding,
        these include the mechanism for breaking ties described in the analysis.
        """
        self.queue.append(data)
        curloc = len(self.queue)-1
        for node in range(len(self.queue)-2, -1, -1):
            if data.frequency > self.queue[node].frequency:
                # highest priority goes first
                self.swap(node, curloc, self.queue[node], data)
                curloc = node

            elif data.frequency == self.queue[node].frequency:

                if isinstance(data, InternalNode) and isinstance(self.queue[node], LeafNode):
                    # InternalNodes go first
                    self.swap(node, curloc, self.queue[node], data)
                    curloc = node
                    continue

                elif data.character[0] > self.queue[node].character[0]:
                    # Internal nodes with lowest first characters go last
                    self.swap(node, curloc, self.queue[node], data)
                    curloc = node
                    continue

    def swap(self, node, curloc, a, b):
        """
        helper method used for swapping items in the queue while en-queuing
        :param node:
        :param curloc:
        :param a:
        :param b:
        :return:
        """
        temp = a
        self.queue[node] = b
        self.queue[curloc] = temp

    def dequeue(self):
        """
        method used to remove items from the priority queue. In this instance, the lowest priority item is required,
         and therefore, the method pops the last item in the queue (the one with the lowest priority)
        :return: node
        """
        return self.queue.pop()
