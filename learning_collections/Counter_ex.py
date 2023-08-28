from collections import Counter


if __name__ == '__main__':
    inventory = Counter()

    loot = {'sword': 1, 'bread': 3}
    inventory.update(loot)
    print(inventory)

    more_loot = {'sword': 1, 'apple': 1}
    inventory.update(more_loot)
    print(inventory)

    print(len(inventory))
    print(sum(inventory.values()))
