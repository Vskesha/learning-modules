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


def choise_sort(lst):
    """choice sorting in list"""
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


def count_sort(lst):
    """sorting by counting"""
    max = lst[0]  # finding maximal element in given list
    for n in lst:
        if n > max:
            max = n
    aux = [0] * (max + 1)  # creating auxilary list in which
    for n in lst:  # indexes are the unique elements in given list and
        aux[n] += 1  # values are numbers of occurences
    i = 0  # index for writing in lst
    for index in range(len(aux)):
        for k in range(aux[index]):
            lst[i] = index
            i += 1


''' Other variant of implementation
    D = {}
    for n in lst:
        D[n] = D[n] + 1 if n in D else 1
    lst.clear()
    for el in sorted(D.keys()):
        for k in range(D[el]):
            lst.append(el)
'''


def test(algorythm):
    print(f'Testing {algorythm.__name__}')

    list1 = [5, 4, 3, 2, 1]
    # print('First list ', list1)
    algorythm(list1)
    # print('Sorted first list ', list1)
    if list1 == [1, 2, 3, 4, 5]:
        print('Test 1 passed')
    else:
        print('Test 1 failed')

    list1 = [8, 4, 6, 9, 2, 1, 7, 5, 3, 0, 4, 4, 8, 7, 3, 9, 0, 3, 5, 7]
    # print('First list ', list1)
    algorythm(list1)
    # print('Sorted first list ', list1)
    if list1 == [0, 0, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8, 9, 9]:
        print('Test 2 passed')
    else:
        print('Test 2 failed')
    print()


if __name__ == '__main__':
    algorythms = [bubble_sort, insert_sort, choise_sort, count_sort]
    for algorythm in algorythms:
        test(algorythm)
