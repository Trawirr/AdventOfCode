from input_utils import load_input

# PART I

TYPES = (
    (5,),
    (4, 1),
    (3, 2),
    (3, 1, 1),
    (2, 2, 1),
    (2, 1, 1, 1),
    (1, 1, 1, 1, 1)
)

CARDS = 'AKQJT98765432'

def find_type(hand: str, joker: str = '') -> int:
    cards_counter = {}
    jokers = 0
    for card in hand:
        if card == joker: jokers += 1
        else: cards_counter[card] = cards_counter[card] + 1 if card in cards_counter.keys() else 1
    hand_type = list(sorted(cards_counter.values(), key=lambda x: -x)) if cards_counter.values() else [0]
    print(hand_type, jokers, end=" => ")
    hand_type[0] += jokers
    print(hand_type, end=" => ")
    hand_type = tuple(hand_type)
    for i, t in enumerate(TYPES):
        if hand_type == t:
            print(i)
            return i
            
def get_order(hand: str, joker: str = '') -> int:
    if joker: cards = CARDS.replace(joker, '') + joker
    else: cards = CARDS
    return int(''.join([f'{len(cards) - cards.index(c):x}' for c in hand]), 16)

hands_bids = []
for hand_bid in load_input().splitlines():
    hand, bid = hand_bid.split()
    hands_bids.append([find_type(hand), get_order(hand), int(bid)])

hands_bids.sort(key=lambda h: (h[0], -h[1]), reverse=True)

product = 0
for i, hob in enumerate(hands_bids):
    product += (i + 1) * hob[2]
print("Result 1:", product)

# PART II

hands_bids = []
for hand_bid in load_input().splitlines():
    hand, bid = hand_bid.split()
    hands_bids.append([find_type(hand, 'J'), get_order(hand, 'J'), int(bid)])

hands_bids.sort(key=lambda h: (h[0], -h[1]), reverse=True)

product = 0
for i, hob in enumerate(hands_bids):
    product += (i + 1) * hob[2]
print("Result 2:", product)