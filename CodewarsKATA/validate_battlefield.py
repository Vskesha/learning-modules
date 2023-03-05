def validate_battlefield(field: list):
    # add empty cells around battlefield. So we have grid 12X12
    for row in field:
        row.insert(0, 0)
        row.append(0)
    field.insert(0, [0 for _ in range(12)])
    field.append([0 for _ in range(12)])

    ships_left = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]  # ships left to find

    for i in range(1, 11):
        for j in range(1, 11):
            if not field[i][j]:  # Skip current cell if it is empty
                continue
            is_horizontal = field[i][j + 1] == 1  # True if ship is horizontal, False if vertical
            size = 0
            y, x = i, j
            while field[y][x]:  # Looping to calculate size of ship
                size += 1
                field[y][x] = 0  # Replace each cell of ship in order to not check it again
                if is_horizontal:
                    x += 1
                else:
                    y += 1
            if size in ships_left:
                ships_left.remove(size)  # Removing current ship from list
            else:
                return False  #
            boundaries = [field[i][j-1], field[i][j+size]] if is_horizontal else [field[i-1][j], field[i+size][j]]
            boundaries += [field[i-1][j-1+k] if is_horizontal else field[i-1+k][j-1] for k in range(size+2)]
            boundaries += [field[i+1][j-1+k] if is_horizontal else field[i-1+k][j+1] for k in range(size+2)]
            if any(boundaries):
                return False
    if ships_left:
        return False
    return True


if __name__ == '__main__':
    battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(validate_battlefield(battle_field))
