from SourceCode.readfiles import readfreq
from SourceCode.priorityqueue import PriorityQueue
from SourceCode.nodes import LeafNode, InternalNode



def createhuffman(ft: dict):
    """
    calls the priority queue class and creates a new priority queue with all of the leaf nodes. Then it builds a series
    of internal nodes by popping the last two items in the priority queue and assigning them to the left or right
    according to the mechanism for breaking ties. The internal node is then en-queued in the priority queue.
    The loop finishes once the priority queue only contains one internal node (the root node).
    The function returns the root internal node.
    :param ft:
    :return:
    """
    # make a priority queue of nodes
    nodes = PriorityQueue()

    sum = 0
    for f in ft:
        newleaf = LeafNode(f, ft[f])
        nodes.enqueue(newleaf)
        sum += ft[f]

    # make parent nodes up to the root
    while len(nodes.queue) > 1:
        A = nodes.dequeue()
        B = nodes.dequeue()

        if A.frequency > B.frequency:
            # Largest to the right
            left = B
            right = A
        if A.frequency < B.frequency:
            # Largest to the right
            left = A
            right = B
        elif isinstance(A, InternalNode) and isinstance(B, LeafNode):
            left = B
            right = A
        elif isinstance(A, LeafNode) and isinstance(B, InternalNode):
            left = A
            right = B
        elif A.character[0] > B.character[0]:
            left = A
            right = B
        else:
            left = A
            right = B


        # make a parent for the two nodes
        freqsum = right.frequency + left.frequency
        parent = InternalNode(freqsum, left, right)
        if parent.character is None:
            parent.character = left.character + right.character
        else:
            parent.character += left.character + right.character
        temp_character = sorted(parent.character)
        parent.character = ''.join(temp_character)

        nodes.enqueue(parent)

    return nodes.dequeue()


def gethuffmancodes(node,prefix,output):
    """
    recursively traverses the tree and creates a dictionary with all of the leaf nodes in the tree along as
     keys and the corresponding code.
    :param node:
    :param prefix:
    :param output:
    :return:
    """
    if isinstance(node,LeafNode):
        output[node.character] = prefix
    else:
        gethuffmancodes(node.left, prefix + '0', output)
        gethuffmancodes(node.right, prefix + '1', output)
    return output


def preorderhuffman(root: InternalNode, level: int = 0):
    """
    preorder traversal of tree. It prints out the output from left to right on the screen
    :param root: Node of Huffman Tree
    :param level: Integer used for printout
    """
    # if root is None return
    if root==None:
        return
    # traverse left subtree
    preorderhuffman(root.left, level + 1)
    # traverse root
    print(' ' * 10 * level + '->' + root.__str__())
    # traverse right subtree
    preorderhuffman(root.right, level + 1)

def compresshuffman(huffmancode:dict, stringlist: list) -> list:
    """
    uses the huffmancodes to create a list of the compression codes.
    :param huffmancode:
    :param stringlist:
    :return:
    """
    encoded = []
    for string in stringlist:
        try:
            encoded.append(huffmancode[string])
        except:
            continue
    return encoded

def decompresshuffman(huffmanroot: InternalNode, compressedstring: str) -> str:
    node = huffmanroot
    result = ''
    for bit in compressedstring:
        # go to left on right child based on bit value
        if bit == '0':
            node = node.left
        else:
            node = node.right
        # if the node is a lead, add the character to the
        # decompressed result and go back to the root node
        if isinstance(node,LeafNode):
            result += node.character
            node = huffmanroot
    return result


if __name__ == "__main__":
    ft = readfreq('../Input/FreqTable.txt')
    huffmanroot = createhuffman(ft)
    preorderhuffman(huffmanroot)
    codes = gethuffmancodes(huffmanroot,'',{})
    string = 'HELLOWORLD'.upper()
    liststring = [x for x in string]
    compress = ''.join(compresshuffman(codes,liststring))
    decompress = decompresshuffman(huffmanroot,'10110000101010011011101101100010110010101100010111000110111')


