from input_utils import load_input
from string import digits

# PART I

def is_adjacent_to_symbol(line, char, height, width):
    not_symbols = digits + '.'
    for d_line in range(-1, 2):
        for d_char in range(-1, 2):
            if 0 <= line + d_line < height and 0 <= char + d_char < width and data[line + d_line][char + d_char] not in not_symbols:
                return True
    return False


data = load_input().splitlines()
height = len(data)
width = len(data[0])

numbers_sum = 0

in_number = False
adjacent_to_symbol = False
number = []
for l, line in enumerate(data):
    for c, char in enumerate(line):
        if char.isnumeric():
            in_number = True
            number.append(char)
            if not adjacent_to_symbol:
                adjacent_to_symbol = is_adjacent_to_symbol(l, c, height, width)
        if not char.isnumeric() or c == width-1:
            if adjacent_to_symbol:
                numbers_sum += int(''.join(number))
            in_number = False
            adjacent_to_symbol = False
            number = []

print("Part 1:", numbers_sum)

# PART II

def get_adjacent_gear(line, char, height, width):
    not_symbols = digits + '.'
    for d_line in range(-1, 2):
        for d_char in range(-1, 2):
            if 0 <= line + d_line < height and 0 <= char + d_char < width and data[line + d_line][char + d_char] not in not_symbols:
                return f"{line + d_line} {char + d_char}"
    return None

gears = {}
height = len(data)
width = len(data[0])

def add_gear_number(gear, number):
    global gears
    if gear in gears.keys():
        gears[gear].append(number)
    else:
        gears[gear] = [number]

in_number = False
adjacent_symbol = None
number = []
for l, line in enumerate(data):
    for c, char in enumerate(line):
        if char.isnumeric():
            in_number = True
            number.append(char)
            if not adjacent_symbol:
                adjacent_symbol = get_adjacent_gear(l, c, height, width)
        if not char.isnumeric() or c == width-1:
            if adjacent_symbol:
                add_gear_number(adjacent_symbol, int(''.join(number)))
            in_number = False
            adjacent_symbol = None
            number = []

gear_ratios_sum = 0
for k, v in gears.items():
    if len(v) == 2:
        gear_ratios_sum += v[0] * v[1]

print("Part 2:", gear_ratios_sum)