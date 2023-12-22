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

# PART II
panel = [list(p) for p in panel]

def tilt_north(panel: list[str]) -> list[str]:
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

# print(f"\n--- Input ---")
# for p in panel: print(p)
for c in range(100000):
    for i in range(4):
        print(c)
        panel = tilt_north(panel)
        panel = rotate_panel(panel)
        # print(f"\n--- Tilt {i+1} ---")
        # for p in panel: print(p)