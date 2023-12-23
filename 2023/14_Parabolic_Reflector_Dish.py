from input_utils import load_input

# PART I

def calculate_rocks(panel: list[str]) -> int:
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
    return int(rocks_sum)

panel = load_input().splitlines()
height = len(panel)

# rocks_sum = 0
# top_limitation = 0
# rocks_counter = 0
# for c in range(len(panel[0])):
#     top_limitation = 0
#     rocks_counter = 0
#     for h in range(height):
#         if panel[h][c] == 'O': rocks_counter += 1
#         if panel[h][c] == '#':
#             rocks_sum += (height - top_limitation + height - top_limitation - rocks_counter + 1) / 2 * rocks_counter
#             rocks_counter = 0
#             top_limitation = h + 1
#     rocks_sum += (height - top_limitation + height - top_limitation - rocks_counter + 1) / 2 * rocks_counter

print("Result 1:", calculate_rocks(panel))

# PART II
#panel = [list(p) for p in panel]

def tilt_north(panel: list[str]) -> list[str]:
    panel = [list(p) for p in panel]
    top_limitation = 0
    rocks_counter = 0
    for c in range(len(panel[0])):
        top_limitation = 0
        rocks_counter = 0
        for h in range(height):
            if panel[h][c] == 'O':
                rocks_counter += 1
                panel[h][c] = '.'

            elif panel[h][c] == '#':
                for i in range(rocks_counter):
                    panel[top_limitation+i][c] = 'O'
                rocks_counter = 0
                top_limitation = h + 1
        for i in range(rocks_counter):
            panel[top_limitation+i][c] = 'O'
    return panel

def rotate_panel(panel: list[str]) -> list[str]:
    new_panel = []
    for i in range(len(panel[0])):
        new_panel_line = [p[-i-1] for p in panel]
        new_panel.append(new_panel_line)

    return new_panel

def calculate_rocks_simple(panel: list[str]):
    height = len(panel)
    rocks_sum = 0
    for h in range(height):
        rocks_sum += (height - h) * panel[h].count('O')

    return int(rocks_sum)

def find_loop(series: list[int]) -> int:
    if len(series) < 3: return None
    for i in range(1, len(series)-1):
        if series[-2 - i] == series[-2]:
            loop_found = True
            for loop_i in range(1, i+1):
                if series[-2 - loop_i] != series[-2 - loop_i - i]:
                    loop_found = False
                    break
            if loop_found and series[-1] == series[-1 - i]:
                return series[-i:]
    return None

cycle_sums = []
# print(f"\n--- Input ---")
# for p in panel: print(p)
for c in range(1000000):
    for i in range(4):
        # print(c)
        panel = tilt_north(panel)
        # print(f"\n--- Cycle {c}, Tilt {i+1} --- {calculate_rocks_simple(panel)}")
        for r in range(3): panel = rotate_panel(panel)
        # for p in panel: print(p)
    #print(f"cycle {c+1}. {calculate_rocks_simple(panel)}")
    cycle_sums.append(calculate_rocks_simple(panel))
    loop = find_loop(cycle_sums)
    if loop is not None:
#        print(loop, (1e9-c-2)%len(loop), '--->', ])
        break