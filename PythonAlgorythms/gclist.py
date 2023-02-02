from random import randint


def lcs(list_a: list, list_b: list):
    """
    calculates length of the longest common subsequences
    :param list_a:
    :param list_b:
    :return: length of the longest common subsequences
    """
    la = len(list_a)
    lb = len(list_b)
    f = [[0*i] * (lb + 1) for i in range(la+1)]
    for i in range(1, la+1):
        for j in range(1, lb+1):
            if list_a[i-1] == list_b[j-1]:
                f[i][j] = 1 + f[i-1][j-1]
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])
    return f[-1][-1]


def find_lcs(list_a: list, list_b: list):
    """
    find all longest common subsequences
    :param list_a:
    :param list_b:
    :return: list of all possible max common subsequences
    """
    la = len(list_a)
    lb = len(list_b)
    lcss = [[[]] * (lb+1) for i in range(la+1)]  # list for storing all combinations
    for i in range(la+1):
        for j in range(lb+1):
            # print(f'i = {i}')
            # print(f'j = {j}')
            lcss[i][j] = []
            if i == 0 or j == 0:  # filling first row and first column with empty lists
                lcss[i][j] = [[]]
                continue
            if list_a[i-1] == list_b[j-1]:  # check if the elements of given lists are equal
                # print(f'Element A[{i-1}]=B[{j-1}]={list_a[i-1]}')
                # print(f'lcss[{i - 1}][{j - 1}] is {lcss[i - 1][j - 1]}, therefore:')
                for sequence in lcss[i-1][j-1]:  # Expand all LCSs with the same element
                    # print(f'seq is {seq}')
                    new_seq = sequence + [list_a[i-1]]
                    # print(f'new_seq is {new_seq}')
                    lcss[i][j].append(new_seq)
                    # print(f'lcss[{i}][{j}] is {lcss[i][j]}')
                # print(f'lcss[{i - 1}][{j - 1}] is {lcss[i - 1][j - 1]}, lcss[{i}][{j}] is {lcss[i][j]}')
            else:  # elements of given sequences are not equal
                # print(f'Element A[{i - 1}] not equal B[{j - 1}]: {list_a[i-1]} not equal {list_b[j-1]}')
                # print(f'lcss[{i-1}][{j}] is {lcss[i-1][j]}; lcss[{i}][{j-1}] is {lcss[i][j-1]}')
                if len(lcss[i-1][j][0]) > len(lcss[i][j-1][0]):  # lcss[i-1][j] has longer subsequences
                    # print(f'Longer subsequences are in lcss[{i-1}][{j}] with length = {len(lcss[i-1][j][0])}')
                    lcss[i][j].extend(lcss[i-1][j])
                elif len(lcss[i-1][j][0]) < len(lcss[i][j-1][0]):  # lcss[i][j-1] has longer subsequences
                    # print(f'Longer subsequences are in lcss[{i}][{j-1}] with length = {len(lcss[i][j-1][0])}')
                    lcss[i][j].extend(lcss[i][j-1])
                elif not lcss[i][j-1][0]:  # lcss top and left are empty
                    # print(f'Sequences on top and on left are empty')
                    lcss[i][j] = [[]]
                else:  # lcss top and left has equal length of subsequences
                    # print(f'Sequences on top and on left are the same length')
                    lcss[i][j].extend(lcss[i-1][j])
                    for sequence in lcss[i][j-1]:
                        if sequence not in lcss[i-1][j]:
                            lcss[i][j].append(sequence)
                # print(f'lcss[{i - 1}][{j}] is {lcss[i - 1][j]}; lcss[{i}][{j - 1}] is {lcss[i][j - 1]}; '
                #       f'lcss[{i}][{j}] is {lcss[i][j]}')
            # for line in lcss:
                # print(*line)
    # print()
    # for line in lcss:
    #     print(*line)
    return lcss[-1][-1]


def lcs_table(list_a, list_b):
    """
    calculates length of the longest common subsequences for all sublist a and sublist b
    :param list_a:
    :param list_b:
    :return: list of the longest common subsequences for all sublist a and sublist b
    """
    la = len(list_a)
    lb = len(list_b)
    f = [[0] * (lb + 1) for i in range(la + 1)]
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            if list_a[i - 1] == list_b[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    return f


def find_lcs2(list_a: list, list_b: list, lena: int = -1, lenb: int = -1, lcs_tab: list = None, lm: int = -1):
    lcs_tab = lcs_tab or lcs_table(list_a, list_b)
    print('lcs tab is:')
    for seq in lcs_tab:
        print(seq)
    if lena == -1:
        lena = len(a)
    if lenb == -1:
        lenb = len(b)
    print(f'lenA = {lena}, lenB = {lenb}')
    if lm == -1:
        lm = lcs_tab[-1][-1]
    print(f'lm = {lm}')
    res_list = []
    print(f'res_list is {res_list}')
    if lm < 1:
        print(f'lm = {lm}. That\'s why we return empty list')
        return [[]]
    for i in range(lena, 0, -1):
        if lcs_tab[i][lenb] < lm:
            print('End finding loop because there are no more combinations')
            break
        for j in range(lenb, 0, -1):
            print(f'i = {i}, j = {j}')
            if lcs_tab[i][j] == lcs_tab[i][j-1] and list_a[i-1] != list_b[j-1]:
                print(f'[{i}][{j}] = [{i}][{j-1}] = {lcs_tab[i][j]}. Moving left to [{i}][{j-1}]')
                continue
            elif lcs_tab[i][j] == lcs_tab[i-1][j] and list_a[i-1] != list_b[j-1]:
                print(f'[{i}][{j}] = [{i-1}][{j}] = {lcs_tab[i][j]}. Moving to upper row')
                break
            else:
                print(f'Values on left and on top are less')
                # recursive calling
                previous_res_list = find_lcs2(list_a, list_b, i-1, j-1, lcs_tab, lm-1)
                print(f'Previous_res_list is: {previous_res_list}')
                add_element = list_a[i-1]
                print(f'Add element is {add_element}, because A[{i-1}]={list_a[i-1]} and B[{j-1}]={list_b[j-1]}')
                for subseq in previous_res_list:
                    res_list.append(subseq + [add_element])
                print(f'res_list is {res_list}')
                break
    # removing duplicates in res_list
    res_list = [el for i, el in enumerate(res_list) if el not in res_list[0:i]]
    # rl = []
    # for i in range(len(res_list)):
    #     flag_is = False
    #     for j in range(i):
    #         if res_list[i] == res_list[j]:
    #             flag_is = True
    #             break
    #     if flag_is:
    #         continue
    #     rl.append(res_list[i])
    # res_list = [*rl]
    return res_list




if __name__ == '__main__':
    n = 8  # size of list 'a'
    m = 10  # size of list 'b'
    # a = [randint(1, 10) for i in range(n)]
    # b = [randint(1, 10) for i in range(m)]
    a = [9, 9, 6, 7, 1, 3, 6, 6]
    b = [2, 4, 7, 6, 3, 10, 1, 6, 4, 9]
    # a = list('abcabcaa')
    # b = list('acbacba')
    # a = [1, 3, 2, 1, 4]
    # b = [3, 1, 2]
    print(a)
    print(b)
    print(f'Maximal length of longest common subsequences is {lcs(a, b)}')
    lc = lcs_table(a, b)
    for lst in lc:
        print(lst)
    sequences = find_lcs(a, b)
    print('Return from find_lcs:')
    for seq in sequences:
        print(seq)
    sequences = find_lcs2(a, b)
    print('Return from find_lcs2')
    for seq in sequences:
        print(seq)
