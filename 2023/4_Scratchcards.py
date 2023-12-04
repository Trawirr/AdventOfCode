from input_utils import load_input

# PART I

def split_numbers(numbers: str) -> list[int]:
    return [int(i) for i in numbers.strip().split()]

points = 0
for card in load_input().splitlines():
    winning_numbers, my_numbers = card.split(": ")[1].split(" | ")
    winning_numbers = split_numbers(winning_numbers)
    my_numbers = split_numbers(my_numbers)
    
    counter = 0
    for winning_number in winning_numbers:
        if winning_number in my_numbers: counter += 1
    if counter > 0: points += 2**(counter-1)

print("Result 1:", points)

# PART II

cards_list = load_input().splitlines()
cards = {(i+1):1 for i in range(len(cards_list))}
for i, card in enumerate(cards_list):
    if not i + 1 in cards.keys():
        break
    winning_numbers, my_numbers = card.split(": ")[1].split(" | ")
    winning_numbers = split_numbers(winning_numbers)
    my_numbers = split_numbers(my_numbers)
    
    counter = 0
    for winning_number in winning_numbers:
        if winning_number in my_numbers: counter += 1
    for c in range(counter):
        card_index = i + 1 + c + 1
        if card_index in cards.keys():
            cards[card_index] += cards[i+1]
        else:
            cards[card_index] = cards[i+1]
        
print("Result 2:", sum(cards.values()))