from input_utils import load_input

# PART I

# (0, 0) - top left corner
TILES = {
    '|': ('y-1', 'y+1'),
    '-': ('x-1', 'x+1'),
    'L': ('y-1', 'x+1'),
    'J': ('y-1', 'x-1'),
    '7': ('y+1', 'x-1'),
    'F': ('y+1', 'x+1'),
    'S': ('y-1', 'y+1', 'x-1', 'x+1'),
    '.': ()
}

def get_tile_diffs(tile: str) -> list:
    tile_diffs = []
    for diff in TILES[tile]:
        d = (int(diff[1:]), 0) if diff[0] == 'x' else (0, int(diff[1:]))
        tile_diffs.append(d)
    return tile_diffs

def get_adjacent_tiles(xy: tuple[int], tile, size_x, size_y):
    current_tiles = xy
    coords = []
    for diff in get_tile_diffs(tile):
        x, y = current_tiles[0] + diff[0], current_tiles[1] + diff[1]
        if x >= size_x or x < 0 or y < 0 or y >= size_y:
            continue
        coords.append((x, y))
    return coords

def find_S(maze):
    for y, maze_line in enumerate(maze):
        for x, maze_cell in enumerate(maze_line):
            if maze_cell == 'S': return (x, y)

maze = load_input().splitlines()
maze_steps = [[0 if maze_cell != '.' else -1  for maze_cell in maze_line] for maze_line in maze]
size_x, size_y = len(maze[0]), len(maze)

max_distance = 0
s_tile = find_S(maze)
to_visit = [s_tile]
visited = []
while to_visit:
    current_tile = to_visit.pop(len(to_visit)-1)
    visited.append(current_tile)
    x0, y0 = current_tile
    adjacent_tiles = get_adjacent_tiles(current_tile, maze[y0][x0], size_x, size_y)
    for x, y in adjacent_tiles:
        if not current_tile in get_adjacent_tiles((x, y), maze[y][x], size_x, size_y):
            continue
        if (maze_steps[y][x] == 0 and (x, y) not in visited):
            to_visit.insert(0, (x, y))
            maze_steps[y][x] = maze_steps[y0][x0] + 1
        max_distance = max(max_distance, maze_steps[y][x])
print("Result 1:", max([max(m) for m in maze_steps]))

# PART II

def get_adjacent_empty_tiles(x: float, y: float, maze: list):
    tiles = [
        (int(x), int(y)),
        (int(x+1), int(y)),
        (int(x), int(y+1)),
        (int(x+1), int(y+1))
    ]
    tiles = [t for t in tiles if is_in_maze(t[0], t[1], size_x, size_y)]
    return [t for t in tiles if maze[t[1]][t[0]] == '.']

def is_connected(xy1, xy2, size_x, size_y):
    if not is_in_maze(xy1[0], xy1[1], size_x, size_y):
        is_connected1 = True
    else:
        is_connected1 = xy2 in get_adjacent_tiles(xy1, maze[xy1[1]][xy1[0]], size_x, size_y)

    if not is_in_maze(xy2[0], xy2[1], size_x, size_y):
        is_connected2 = True
    else:
        is_connected2 = xy1 in get_adjacent_tiles(xy2, maze[xy2[1]][xy2[0]], size_x, size_y)
    
    if is_connected1 and is_connected2:
        return True
    return False

def is_in_maze(x: float, y: float, size_x: int, size_y: int):
    if x >= size_x or x <= -1 or y >= size_y or y <= -1:
        return False
    return True

to_visit = []
for x in range(size_x-1):
    to_visit.append((x+0.5, -0.5))
    to_visit.append((x+0.5, size_y-0.5))

for y in range(size_y-1):
    to_visit.append((-0.5, y+0.5))
    to_visit.append((size_x-0.5, y+0.5))

tiles_count = size_x * size_y
for maze_line in maze:
    for maze_cell in maze_line:
        if maze_cell != '.':
            tiles_count -= 1

visited = []
outside_tiles = []
while to_visit:
    current_tile = to_visit.pop(0)
    visited.append(current_tile)
    x0, y0 = current_tile
    if is_in_maze(x0-1, y, size_x, size_y) and not is_connected((int(x0), int(y0)), (int(x0), int(y0+1)), size_x, size_y):
        if (x0-1, y) not in visited: to_visit.append((x0-1, y))
    if is_in_maze(x0+1, y, size_x, size_y) and not is_connected((int(x0+1), int(y0)), (int(x0+1), int(y0+1)), size_x, size_y):
        if (x0+1, y) not in visited: to_visit.append((x0+1, y))
    if is_in_maze(x0, y-1, size_x, size_y) and not is_connected((int(x0), int(y0)), (int(x0+1), int(y0)), size_x, size_y):
        if (x0, y-1) not in visited: to_visit.append((x0, y-1))
    if is_in_maze(x0, y+1, size_x, size_y) and not is_connected((int(x0), int(y0+1)), (int(x0+1), int(y0+1)), size_x, size_y):
        if (x0, y+1) not in visited: to_visit.append((x0, y+1))

    for tile in get_adjacent_empty_tiles(x0, y0, maze):
        if tile not in outside_tiles:
            outside_tiles.append(tile)

print(tiles_count, len(outside_tiles))