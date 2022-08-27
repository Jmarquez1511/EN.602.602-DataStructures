from SourceCode.readfiles import read_files
import sys
sys.setrecursionlimit(1000000)


def insertion_sort(array, first, last):
    """
    Bsed of the implementation from Miller and Ranum
    https://runestone.academy/ns/books/published/pythonds/SortSearch/TheInsertionSort.html
    :param array:
    :param first:
    :param last:
    :return:
    """
    global c
    global r
    for index in range(first, last):

        currentvalue = array[index]
        position = index

        while position > 0 and array[position - 1] > currentvalue:
            c += 1
            swap(array, position, position - 1)
            r += 1
            position = position - 1

        array[position] = currentvalue


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def quick_sort(array, first, last):
    """
    based of the Lomuto partition scheme https://en.wikipedia.org/wiki/Quicksort
    :param array:
    :param first:
    :param last:
    :return:
    """
    global c
    global r
    # ensure indices are in correct order
    if first >= last or first < 0:
        return

    # partition array and get the pivot index
    pivot = partition(array, first, last)

    # sort the two partitions
    quick_sort(array, first, pivot-1)
    quick_sort(array, pivot+1, last)


def partition(array, first, last):
    """
    Implementation from Miller and Ranum
    https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html
    :param array:
    :param first:
    :param last:
    :return:
    """
    global c
    global r
    pivotvalue = array[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            c += 1
            leftmark = leftmark + 1

        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            c += 1
            rightmark = rightmark -1
        if rightmark < leftmark:
            c += 1
            done = True
        else:
            swap(array,leftmark,rightmark)
            r += 1

    swap(array,first,rightmark)
    r += 1

    return rightmark


def quick_sort_hybrid(array, first, last, number_):
    """
    based off Advanced Quick Sort (Hybrid Algorithm)
    https://www.geeksforgeeks.org/advanced-quick-sort-hybrid-algorithm/
    :param array:
    :param first:
    :param last:
    :param number_:
    :return:
    """
    # ensure indices are in correct order
    # ensure indices are in correct order
    while first < last:
        if last - first + 1 <= number_:
            # if the size of the array is less thant the threshold
            # apply insertion sort and stop recursion
            insertion_sort(array, first, last+1)
            break

        else:
            # perform a quick sort
            pivot = partition(array, first, last)

            if pivot-last < last-pivot:
                quick_sort_hybrid(array, first, pivot-1, number_)
                first = pivot + 1
            else:
                quick_sort_hybrid(array, pivot+1, last, number_)
                last = pivot - 1


def median_of_three(array, first, last):
    """
    from https://stackoverflow.com/questions/50912873/python-quicksort-with-median-of-three
    :param array:
    :param first:
    :param last:
    :return:
    """
    mid = (first+last)//2
    a = array[first]
    b = array[mid]
    c = array[last]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, last
    if b <= c <= a:
        return c, last
    return a, first


def partition_median(array, first, last):
    """
    Implementation from Miller and Ranum
    https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html
    :param array:
    :param first:
    :param last:
    :return:
    """
    global c
    global r
    pivotvalue, pivot_index = median_of_three(array, first, last)
    swap(array, first, pivot_index)
    r += 1

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            c+=1
            leftmark = leftmark + 1

        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
           done = True
        else:
            swap(array, leftmark, rightmark)
            r+=1

    swap(array, first, rightmark)
    r += 1

    return rightmark



def quick_sort_median(array, first, last):
    """
    based of the Lomuto partition scheme https://en.wikipedia.org/wiki/Quicksort
    :param array:
    :param first:
    :param last:
    :return:
    """
    global c
    global r

    # ensure indices are in correct order
    if first >= last or first < 0:
        return

    # partition array and get the pivot index
    pivot = partition_median(array, first, last)

    # sort the two partitions
    quick_sort(array, first, pivot - 1)
    quick_sort(array, pivot + 1, last)


def all_quick_sorts(array, first, last, sort_type):
    global c
    global r
    c = 0
    r = 0
    if sort_type == 1:
        quick_sort(array, first, last)
    elif sort_type == 2:
        quick_sort_hybrid(array, first, last, 50)
    elif sort_type == 3:
        quick_sort_hybrid(array, first, last, 100)
    elif sort_type == 4:
        quick_sort_median(array, first, last)
    elif sort_type == 5:
        quick_sort_hybrid(array, first, last, 10)
    return c, r


if __name__ == "__main__":

    data_sets = read_files('../Input/')
    a_list = list(data_sets['random_50']['list'])
    print(a_list)
    c, r = all_quick_sorts(a_list, 0, len(a_list) - 1, 4)
    print(a_list)
    print(c, r)

    