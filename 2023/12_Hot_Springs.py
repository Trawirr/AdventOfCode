from input_utils import load_input

# PART I

def split_group(springs_group):
    counter = 0
    groups = []
    for s in springs_group:
        if s == '#':
            counter += 1
        else:
            if counter > 0: groups.append(counter)
            counter = 0
    if counter > 0: groups.append(counter)
    return groups

def permute_group(springs_group, permutation):
    counter = 0
    permutated_group = ""
    for s in springs_group:
        if s == '?':
            permutated_group += '.' if permutation[counter] == '1' else '#'
            counter += 1
        else:
            permutated_group += s
    return permutated_group

def get_possibilities(springs_group, groups):
    permutable_places = springs_group.count('?')
    counter = 0
    for i in range(2**permutable_places):
        permutation = '0' * (permutable_places - len(bin(i)[2:])) + bin(i)[2:]
        if split_group(permute_group(springs_group, permutation)) == groups:
            counter += 1
    return counter

springs_data = load_input().splitlines()
posibilities_sum = 0
for spring_line in springs_data:
    print(spring_line)
    springs, groups = spring_line.split()
    springs = '?'.join(springs*5)
    groups = ','.join([groups]*5)
    groups = [int(g) for g in groups.split(',')]
    posibilities_sum += get_possibilities(springs, groups)

print("Result 1:", posibilities_sum)