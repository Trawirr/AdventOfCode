from input_utils import load_input

# PART I

panel = load_input().splitlines()
height = len(panel)

rocks_sum = 0
top_limitation = 0
rocks_counter = 0
for c in range(len(panel[0])):
    top_limitation = 0
    rocks_counter = 0
    for h in range(height):
        if panel[h][c] == 'O': rocks_counter += 1
        if panel[h][c] == '#':
            rocks_sum += (height - top_limitation + height - top_limitation - rocks_counter + 1) / 2 * rocks_counter
            rocks_counter = 0
            top_limitation = h + 1
    rocks_sum += (height - top_limitation + height - top_limitation - rocks_counter + 1) / 2 * rocks_counter

print("Result 1:", int(rocks_sum))