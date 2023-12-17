from input_utils import load_input

# PART I

def predict(sequence):
    sequence = [int(e) for e in sequence.split()]
    diff_sequences = [sequence]
    
    # counting diff_sequences
    for i in range(len(sequence)):
        diff_seq = [diff_sequences[-1][i+1] - diff_sequences[-1][i] for i in range(len(diff_sequences[-1])-1)]
        diff_sequences.append(diff_seq)
        if not [e for e in diff_seq if e != 0]:
            break

    diff_sequences_count = len(diff_sequences)
    for i in range(len(diff_sequences) - 1):
        diff = diff_sequences[diff_sequences_count - 1 - i][-1]
        diff_sequences[diff_sequences_count - 2 - i].append(diff_sequences[diff_sequences_count - 2 - i][-1] + diff)

    return diff_sequences[0][-1]

sequences = load_input().splitlines()
sequences_sum = 0
for sequence in sequences:
    sequences_sum += predict(sequence)

print("Result 1:", sequences_sum)

# PART II

def predict_backwards(sequence):
    sequence = [int(e) for e in sequence.split()]
    diff_sequences = [sequence]
    
    # counting diff_sequences
    for i in range(len(sequence)):
        diff_seq = [diff_sequences[-1][i+1] - diff_sequences[-1][i] for i in range(len(diff_sequences[-1])-1)]
        diff_sequences.append(diff_seq)
        if not [e for e in diff_seq if e != 0]:
            break

    diff_sequences_count = len(diff_sequences)
    for i in range(len(diff_sequences) - 1):
        diff = diff_sequences[diff_sequences_count - 1 - i][0]
        diff_sequences[diff_sequences_count - 2 - i].insert(0, diff_sequences[diff_sequences_count - 2 - i][0] - diff)

    return diff_sequences[0][0]

sequences = load_input().splitlines()
sequences_sum = 0
for sequence in sequences:
    sequences_sum += predict_backwards(sequence)

print("Result 2:", sequences_sum)