def hand(hole_cards, community_cards):
    card_val = {k: k for k in range(2, 10)} | {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    all_cards = hole_cards + community_cards
    all_cards_val = [card_val[c[0]] for c in all_cards]
    return "nothing", ["2", "3", "4", "7", "8"]


if __name__ == '__main__':
    hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]),
    ("nothing", ["A", "K", "Q", "J", "9"]),