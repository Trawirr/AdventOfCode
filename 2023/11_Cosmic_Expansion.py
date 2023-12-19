from input_utils import load_input

# PART I

def distance(galaxy_index1, galaxy_index2, cosmos_weights):
    xs = sorted([galaxy_index1[0], galaxy_index2[0]])
    ys = sorted([galaxy_index1[1], galaxy_index2[1]])
    dist_sum = 0
    # print(cosmos_weights[ys[0]][xs[0]:xs[1]])
    dist_sum += sum(cosmos_weights[ys[0]][xs[0]:xs[1]])
    # print([cosmos_weights[y][xs[0]] for y in range(ys[0], ys[1])])
    dist_sum += sum([cosmos_weights[y][xs[0]] for y in range(ys[0], ys[1])])
    return dist_sum

galaxies = {}
galaxies_count = 0
cosmos_image = load_input().splitlines()

for y, cosmos_line in enumerate(cosmos_image):
    for x, cosmos_tile in enumerate(cosmos_line):
        if cosmos_tile == '#':
            galaxies_count += 1
            galaxies[galaxies_count] = (x, y)

cosmos_weights = [[1 for cosmos_cell in cosmos_line] for cosmos_line in cosmos_image]

for y, cosmos_line in enumerate(cosmos_image):
    if not cosmos_line.replace('.', ''):
        for x in range(len(cosmos_line)):
            cosmos_weights[y][x] = 2
    
for x in range(len(cosmos_image[0])):
    if not ''.join([cosmos_line[x] for cosmos_line in cosmos_image]).replace('.', ''):
        for y in range(len(cosmos_image)):
            cosmos_weights[y][x] = 2

distances_sum = 0
for i in range(galaxies_count):
    for j in range(i+1, galaxies_count):
        distances_sum += distance(galaxies[i+1], galaxies[j+1], cosmos_weights)

print("Result 1:", distances_sum)

# PART II

gap_distance = 1000000

cosmos_weights = [[gap_distance if c > 1 else 1 for c in cosmos_line] for cosmos_line in cosmos_weights]

distances_sum = 0
for i in range(galaxies_count):
    for j in range(i+1, galaxies_count):
        distances_sum += distance(galaxies[i+1], galaxies[j+1], cosmos_weights)

print("Result 1:", distances_sum)