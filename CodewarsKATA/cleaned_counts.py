def cleaned_counts2(data):
    res = data.copy()
    for i in range(1, len(res)):
        if res[i] < res[i - 1]:
            res[i] = res[i - 1]
    return res


cleaned_counts = lambda a, m=0: [m := max(m, n) for n in a]


if __name__ == '__main__':
    print(cleaned_counts([2, 1, 2]), [2, 2, 2])
    print(cleaned_counts([4, 4, 4, 4]), [4, 4, 4, 4])
    print(cleaned_counts([1, 1, 2, 2, 1, 2, 2, 2, 2]), [1, 1, 2, 2, 2, 2, 2, 2, 2])
    print(cleaned_counts([5, 5, 6, 5, 5, 5, 5, 6]), [5, 5, 6, 6, 6, 6, 6, 6])
