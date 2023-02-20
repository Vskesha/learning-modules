def assert_equals(a, b):
        if a == b:
            print('Test completed')
        else:
            print('Test failed')


def sel_reverse(arr, l):
    # first implementation
    # if l > 1:
    #     res = []
    #     for i in range(0, len(arr), l):
    #         res.extend(reversed(arr[i:i + l]))
    #     return res
    # return arr

    # second implementation
    # if l < 2:
    #     return arr
    # res = []
    # for i in range(0, len(arr), l):
    #     for el in arr[i:i+l][::-1]:
    #         res += [el]
    # return res

    # third implementation
    return [elt for i in range(0, len(arr), l) for elt in arr[i:i+l][::-1]] if l > 1 else arr


if __name__ == '__main__':
    assert_equals(sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 3), [6, 4, 2, 12, 10, 8, 16, 14])
    assert_equals(sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 2), [4, 2, 8, 6, 12, 10, 16, 14])
    assert_equals(sel_reverse([1, 2, 3, 4, 5, 6], 2), [2, 1, 4, 3, 6, 5])
    assert_equals(sel_reverse([1, 2, 3, 4, 5, 6], 0), [1, 2, 3, 4, 5, 6])
    assert_equals(sel_reverse([1, 2, 3, 4, 5, 6], 10), [6, 5, 4, 3, 2, 1])