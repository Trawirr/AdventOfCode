from input_utils import load_input

# PART I

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def get_adjacent_tiles(x: int, y: int, size_x: int, size_y: int):
    adjacent_tiles = [(x+dx, y+dy) for dx, dy in DIRECTIONS if 0 <= x+dx < size_x and 0 <= y+dy < size_y]
    return adjacent_tiles

def check_direction(x: int, y: int):
    pass

grid = load_input().splitlines()
grid_directions = [[(0, 0, 0) for g in grid_line] for grid_line in grid]
start = [0, 0]
width = len(grid[0])
height = len(grid)
finish = [width-1, height-1]

to_visit = [start]
while to_visit:
    current_node = to_visit.pop(0)
    x, y = current_node
    adjacent_tiles = get_adjacent_tiles(x, y, width, height)
    for adjacent_tile in adjacent_tiles:
        x_adj, y_adj = adjacent_tile
        dx, dy = adjacent_tile[0] - current_node[0], adjacent_tile[1] - current_node[1]
        grid_distance, grid_dx, grid_dy = grid_directions[current_node[1]][current_node[0]]
        new_distance = grid_distance + grid_directions[y][x][0]
        if new_distance < grid_directions[y_adj][x_adj][0]:
            update_node = True
            new_dx, new_dy = dx, dy
            if dx != 0 and grid_dx != 0:
                if abs(dx + grid_dx) > 3:
                    update_node = False
                else:
                    new_dx = dx + grid_dx
            elif dy != 0 and grid_dy != 0:
                if abs(dy + grid_dy) > 3:
                    update_node = False
                else:
                    new_dy = dy + grid_dy
            if update_node:
                grid_directions[y_adj][x_adj] = [new_distance, new_dx, new_dy]
                to_visit.append(adjacent_tile)

print(grid_directions[finish[1]][finish[0]])