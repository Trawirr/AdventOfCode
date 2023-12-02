from input_utils import load_input

# PART I

CUBES_MAX = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_cubes(pull: str) -> dict:
    pull = pull.strip().split(', ')
    return {k: int(v) for v, k in [p.split() for p in pull]}


def check_game(cubes: dict) -> bool:
    for k, v in cubes.items():
        if v > CUBES_MAX[k]: return False
    return True

sum_id = 0
for i, input_line in enumerate(load_input().splitlines()):
    pulls = input_line.split(": ")[1].split(";")
    game_possible = True
    for pull in pulls:
        if not check_game(parse_cubes(pull)):
            game_possible = False
            break
    if game_possible:
        sum_id += i+1
print("Part I:", sum_id)

# PART II

CUBES_MAX = {
    "red": 0,
    "green": 0,
    "blue": 0
}

CUBES_SUM = 0

def parse_cubes(pull: str) -> dict:
    pull = pull.strip().split(', ')
    return {k: int(v) for v, k in [p.split() for p in pull]}

def set_cubes_max(cubes: dict) -> bool:
    global CUBES_MAX
    for k, v in cubes.items():
        CUBES_MAX[k] = max(CUBES_MAX[k], v)

def clear_cubes_max() -> None:
    global CUBES_MAX
    for k in CUBES_MAX.keys():
        CUBES_MAX[k] = 0

def add_cubes_max() -> None:
    global CUBES_MAX
    global CUBES_SUM
    product = 1
    for k in CUBES_MAX.keys():
        product *= CUBES_MAX[k]
    CUBES_SUM += product

sum_id = 0
for i, input_line in enumerate(load_input().splitlines()):
    pulls = input_line.split(": ")[1].split(";")
    game_possible = True
    for pull in pulls:
        set_cubes_max(parse_cubes(pull))
    add_cubes_max()
    clear_cubes_max()
print("Part II:", CUBES_SUM)