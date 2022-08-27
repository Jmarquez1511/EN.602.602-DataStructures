from SourceCode.readfiles import read_files
#!/usr/bin/env python
"""Merge sort a singly linked linear list."""

# Linked list is either empty or a data and a link to the next list
empty = None # empty list

c, r = 0, 0

def merge_sort(head):
    """Translation from C to Python of listsort() [1].

    O(N log N) (best & worst) -time, O(1)-space
    inplace Mergesort algorithm for a singly linked linear list [2]

    [1]: http://www.chiark.greenend.org.uk/~sgtatham/algorithms/listsort.c
    [2]: http://www.chiark.greenend.org.uk/~sgtatham/algorithms/listsort.html
    """
    global c
    global r

    c = 0
    r = 0

    insize = 1 # lists of size 1 are always sorted
    while True: # merge adjacent pairs of `insize`-sized sorted lists
        p = head # head of the left list to be merged
        head, tail = empty, empty # head and tail of the output list
        nmerges = 0 # count number of merges we do in this pass
        c += 1
        while p is not empty:
            nmerges += 1 # there exists a merge to be done
            c += 1
            # step `insize' places along from p or until the end of
            #   the list, whichever comes first
            q = p # head of the right list to be merged
            for psize in range(1, insize + 1):
                q = q.next
                if q is empty: # the end of the list (q is empty list)
                    break
            qsize = insize

            # merge a list starting at p, of length psize, with a list
            #  starting at q of length *at most* qsize
            while psize > 0 or (qsize > 0 and q is not empty):
                # decide whether next element of merge comes from p or q
                if psize == 0: # p is empty
                    e, q = q, q.next # e must come from q, pop q
                    r += 1
                    qsize -= 1
                elif qsize == 0 or q is empty: # q is empty
                    e, p = p, p.next # e must come from p, pop p
                    r += 1
                    psize -= 1
                elif p.data <= q.data: # first element of p is lower or same
                    # choose p in the case of `p.data == q.data` to
                    # maintain sort stability
                    e, p = p, p.next # e must come from p, pop p
                    r += 1
                    psize -= 1
                else: # p.data > q.data i.e., first element of q is lower
                    e, q = q, q.next # e must come from q, pop q
                    r += 1
                    qsize -= 1

                # add e to the end of the output list
                if tail is not empty:
                    tail.next = e
                else: # 1st iteration
                    head = e # smallest item among two lists
                tail = e
            # now p has stepped `insize' places along, and q has too (or eol)
            p = q # move to the next pair of lists to merge
        #end of while p is not empty:

        if tail is not empty:
            tail.next = empty # terminate the output list

        # if we have done only one merge, we're finished
        if nmerges <= 1: # allow for nmerges==0, the empty list case
            return head, c,r
        else:# otherwise repeat, merging lists twice the size
            insize *= 2


def find_next_stop(head):
    global c
    global r

    if head is empty:
        return head, 0, empty
    next_node = head.next
    if next_node is empty:
        return head, 1, empty

    size = 2

    if head <= next_node:
        c += 1
        while(next_node.next and next_node <= next_node.next):
            c += 1
            size += 1
            next_node = next_node.next
        next_node = next_node.next
    else:
        while(next_node.next and next_node.next < next_node):
            c += 1
            size += 1
            next_node = next_node.next
        next_node = next_node.next
        head = reverse(head, size)

    return head, size, next_node

def reverse(head, size=-1):
    global r
    """
    reference: https://stackoverflow.com/a/22049871/3552
    """
    new_head = None
    while head:
        temp = head
        head = temp.next
        temp.next = new_head
        new_head = temp
        r += 1

        size-=1
        if not size:
            tail = new_head
            while tail.next:
                tail = tail.next
            tail.next = head
            return new_head

    return new_head


def natural_merge_sort(head):
    """
    Revising from mergesort-linkedlist to Natural_mergesort_linkedlist [1].
    https://codereview.stackexchange.com/questions/211149/linked-list-natural-merge-sort-in-python
    Original merge sort: https://gist.github.com/zed/5651186
    """
    global r
    global c
    c = 0
    r = 0
    p = q = head
    psize = 0
    tail = empty

    while q is not empty:
        tail = empty
        q, qsize, next_q = find_next_stop(q)
        msize = psize + qsize

        while qsize > 0 or psize > 0:
            if psize == 0:
                e, q = q, q.next
                r += 1
                qsize -= 1
            elif qsize == 0:
                e, p = p, p.next
                psize -= 1
                r += 1
            elif p <= q:
                e, p = p, p.next
                psize -= 1
                r += 1
            else:
                e, q = q, q.next
                qsize -= 1
                r += 1

            if tail is empty:
                head = e
            else:
                tail.next = e
            tail = e

        psize = msize
        q = next_q
        p = head

    if tail is not empty:
        tail.next = empty

    return head, c, r


if __name__ == "__main__":
    data_sets = read_files('../Input/')
    head = data_sets['ascending_100']['linked_list'].head
    head, c, r = natural_merge_sort(head)
    print(c, r)
    list_= list(head.make_list())
    print(list_)

    head_ = data_sets['ascending_100']['linked_list'].head
    head_, c, r = merge_sort(head)
    print(c, r)
    list_ = list(head_.make_list())
    print(list_)



