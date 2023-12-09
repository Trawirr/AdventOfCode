from input_utils import load_input

# PART I

data = load_input().splitlines()
instructions = data[0]
map_network = data[2:]

map_nodes = {}
for map_node in map_network:
    source_node, destination_nodes = map_node.split(" = ")
    map_nodes[source_node] = destination_nodes[1:-1].split(', ')

node = 'AAA'
steps = 0
exit_found = False
while not exit_found:
    for instruction in instructions:
        if instruction == "L":
            node = map_nodes[node][0]
        else:
            node = map_nodes[node][1]
        steps += 1
        if node == 'ZZZ':
            exit_found = True
            break

print("Result 1:", steps)
            
# PART II

def find_loop(node, map_nodes, instructions):
    i = 0
    start_node = node
    instructions_loop = instructions
    nodes_loop = [node]
    loop_found = False
    while not loop_found:
        if i >= len(instructions_loop): instructions_loop += instructions
        if instructions_loop[i] == 'L':
            node = map_nodes[node][0]
        else:
            node = map_nodes[node][1]
        if node == start_node:
            break
        i += 1
    return i

nodes = [n for n in map_nodes.keys() if n.endswith('A')]
for node in nodes:
    print(node, find_loop(node, map_nodes, instructions))

# data = load_input().splitlines()
# instructions = data[0]
# map_network = data[2:]

# map_nodes = {}
# for map_node in map_network:
#     source_node, destination_nodes = map_node.split(" = ")
#     map_nodes[source_node] = destination_nodes[1:-1].split(', ')

# nodes = [n for n in map_nodes.keys() if n.endswith('A')]
# steps = 0
# exit_found = False
# while not exit_found:
#     for instruction in instructions:
#         for i in range(len(nodes)):
#             if instruction == "L":
#                 nodes[i] = map_nodes[nodes[i]][0]
#             else:
#                 nodes[i] = map_nodes[nodes[i]][1]
#         steps += 1
#         # print(instruction, nodes)
#         if len([n for n in nodes if not n.endswith('Z')]) <= 2:
#             print(len([n for n in nodes if not n.endswith('Z')]))
#         if not len([n for n in nodes if not n.endswith('Z')]):
#             exit_found = True
#             break

print("Result 2:", steps)
