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


def test(sort_algorithm):
    print(f'Testing {sort_algorithm.__name__}')

    list1 = [5, 4, 3, 2, 1]
    # print('First list ', list1)
    sort_algorithm(list1)
    # print('Sorted first list ', list1)
    if list1 == [1, 2, 3, 4, 5]:
        print('Test 1 passed')
    else:
        print('Test 1 failed')

    list1 = [8, 4, 6, 9, 2, 1, 7, 5, 3, 0, 4, 4, 8, 7, 3, 9, 0, 3, 5, 7]
    # print('First list ', list1)
    sort_algorithm(list1)
    # print('Sorted first list ', list1)
    if list1 == [0, 0, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8, 9, 9]:
        print('Test 2 passed')
    else:
        print('Test 2 failed')
    print()


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


if __name__ == '__main__':
    sorting_algorithms = [bubble_sort, insert_sort, choice_sort, count_sort, quicksort_hoare, quicksort_joining, sorted]
    for algorythm in sorting_algorithms:
        test(algorythm)
