def recoverSecret(triplets):
    result = list(set([ch for triplet in triplets for ch in triplet]))
    for _ in range(3):
        for triplet in triplets:
            indexes_of_result = sorted([result.index(triplet[i]) for i in range(3)])
            for i, index in enumerate(indexes_of_result):
                result[index] = triplet[i]
    return ''.join(result)


if __name__ == '__main__':
    secret = "whatisup"
    triplets = [
        ['t','u','p'],
        ['w','h','i'],
        ['t','s','u'],
        ['a','t','s'],
        ['h','a','p'],
        ['t','i','s'],
        ['w','h','s']
    ]
    print(recoverSecret(triplets))
