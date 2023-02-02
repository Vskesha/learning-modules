import random


def bubble_sort(lst):
    """bubble sorting in list"""
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def insert_sort(lst):
    """insert sorting in list"""
    for i in range(1, len(lst)):
        k = i
        while k > 0 and lst[k] < lst[k - 1]:
            lst[k], lst[k - 1] = lst[k - 1], lst[k]
            k -= 1


def choice_sort(lst):
    """choice sorting in list"""
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


def count_sort(lst):
    """sorting by counting"""
    maximum = lst[0]  # finding maximal element in given list
    for n in lst:
        if n > maximum:
            maximum = n
    aux = [0] * (maximum + 1)  # creating auxiliary list in which
    for n in lst:  # indexes are the unique elements in given list and
        aux[n] += 1  # values are numbers of occurrences
    i = 0  # index for writing in lst
    for index in range(len(aux)):
        for k in range(aux[index]):
            lst[i] = index
            i += 1


def test(sort_algorithm, test_sequences: list):
    """
    Checks different sorting algorithms on given 'sequences'
    :param sort_algorithm:
    :param test_sequences:
    :return: None
    """
    print(f'Testing {sort_algorithm.__name__}')
    for i, sequence in enumerate(test_sequences):
        #print(sequence)
        sec = list(sequence)
        sort_algorithm(sec)
        print(f'Test {i+1} ', end='')
        if check_sorted(sec):
            print('passed')
        else:
            print('failed')
    print()


def check_sorted(a: list, ascending=True):
    """
    Checks list 'list_a' is sorted in ascending or descending order (Time is O(len(list_a))
    :param a: list that will be checked
    :param ascending: True if we check ascending order and False if we check descending order
    :return: boolean (True or False)
    """
    s = 2 * int(ascending) - 1
    flag = True
    for i in range(0, len(a)-1):
        if s * a[i] > s * a[i+1]:
            flag = False
            break
    return flag


def quicksort_hoare(lst: list, start_pos: int = 0, end_pos: int = -1):
    """
    quick recursive sorting by Hoare partition
    :param lst: list that will be sorted
    :param start_pos: start position of sorting
    :param end_pos: end position of sorting
    :return: None
    """
    end_pos = (len(lst) + end_pos) % len(lst)  # makes end position > 0
    if end_pos - start_pos < 1:  # if one or zero elements need to sort
        return
    end1 = start_pos
    start2 = start_pos
    middle = lst[start_pos]
    for i in range(start_pos, end_pos + 1):
        if lst[i] < middle:
            for j in range(i, end1, -1):                # el = lst.pop(i)
                lst[j], lst[j-1] = lst[j-1], lst[j]  # lst.insert(end1, el)
            end1 += 1
            start2 += 1
        elif lst[i] == middle:
            for j in range(i, start2, -1):                # el = lst.pop(i)
                lst[j], lst[j-1] = lst[j-1], lst[j]  # lst.insert(start2, el)
            start2 += 1
    quicksort_hoare(lst, start_pos, end1)
    quicksort_hoare(lst, start2, end_pos)


def hoar_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    l, m, r = [], [], []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    hoar_sort(l)
    hoar_sort(r)
    k = 0
    for x in l + m + r:
        a[k] = x
        k += 1


def quicksort_joining(lst: list):
    """
    quick recursive sorting by joining
    :param lst: list that will be sorted
    :return: None
    """
    if len(lst) <= 1:
        return lst
    i = 0
    j = 0
    k = 0
    list1 = quicksort_joining(lst[0:len(lst)//2])
    list2 = quicksort_joining(lst[len(lst)//2:len(lst)])
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            lst[k] = list1[i]
            k += 1
            i += 1
        else:
            lst[k] = list2[j]
            k += 1
            j += 1
    while i < len(list1):
        lst[k] = list1[i]
        k += 1
        i += 1
    while j < len(list2):
        lst[k] = list2[j]
        k += 1
        j += 1
    return lst


def merge(a: list, b: list):
    c = [0]*(len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(a):
    if len(a) <= 1:
        return
    middle = len(a)//2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(a)):
        a[i] = c[i]


if __name__ == '__main__':
    sorting_algorithms = [bubble_sort,
                          insert_sort,
                          choice_sort,
                          count_sort,
                          quicksort_hoare,
                          quicksort_joining,
                          merge_sort,
                          hoar_sort]
    sequences = [[5, 4, 3, 2, 1],
                 [8, 4, 6, 9, 2, 1, 7, 5, 3, 0, 4, 4, 8, 7, 3, 9, 0, 3, 5, 7],
                 [random.randint(1, 40) for i in range(100)]]
    for algorythm in sorting_algorithms:
        test(algorythm, sequences)
