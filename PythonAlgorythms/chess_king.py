def count_trajectories(n: int, m: int):
    count = [[0] * m for x in range(n)]
    for i in range(m):
        count[0][i] = 1
    for j in range(1, n):
        count[j][0] = 1
    for lst in count:
        print(lst)
    print()
    for i in range(1, n):
        for j in range(1, m):
            count[i][j] = count[i][j-1] + count[i-1][j]
    for lst in count:
        print(lst)
    return count[n-1][m-1]


if __name__ == '__main__':
    print(count_trajectories(8, 6))
