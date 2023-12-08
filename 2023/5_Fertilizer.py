from input_utils import load_input

# PART I

data = load_input().splitlines()

# Parse seeds
seeds = data[0].split(":")[1].split()
seeds_dict = {s:{"seed":int(s)} for s in seeds}
data = data[2:]

print(seeds_dict)

for line in data:
    if ":" in line:
        source, destination = line.split()[0].split("-to-")
        for seed in seeds:
            seeds_dict[seed][destination] = seeds_dict[seed][source]
    elif line:
        destination_start, source_start, range_length = [int(p) for p in line.split()]
        for seed in seeds:
            if source_start <= seeds_dict[seed][source] < source_start + range_length:
                seeds_dict[seed][destination] = destination_start + seeds_dict[seed][source] - source_start

print("Result I:", min([s["location"] for s in seeds_dict.values()]))

# PART II

data = load_input().splitlines()

# Parse seeds
seeds_all = data[0].split(":")[1].split()
seeds = []
for i in range(len(seeds_all)//2):
    for s in range(int(seeds_all[2*i]), int(seeds_all[2*i]) + int(seeds_all[2*i+1])):
        seeds.append(str(s))
seeds_dict = {s:{"seed":int(s)} for s in seeds}

for line in data:
    if ":" in line:
        source, destination = line.split()[0].split("-to-")
        for seed in seeds:
            seeds_dict[seed][destination] = seeds_dict[seed][source]
    elif line:
        destination_start, source_start, range_length = [int(p) for p in line.split()]
        for seed in seeds:
            if source_start <= seeds_dict[seed][source] < source_start + range_length:
                seeds_dict[seed][destination] = destination_start + seeds_dict[seed][source] - source_start

print("Result II:", min([s["location"] for s in seeds_dict.values()]))