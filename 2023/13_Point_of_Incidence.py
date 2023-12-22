from input_utils import load_input

# PART I

def validate_pattern_line(pattern_line: str) -> bool:
    for i in range(len(pattern_line)//2):
        if pattern_line[i] != pattern_line[-1-i]:
            return False
    return True

def validate_pattern(pattern: list[str], start: int, end: int, is_horizontal: bool) -> bool:
    if is_horizontal:
        for pattern_line in pattern:
            if not validate_pattern_line(pattern_line[start:end]):
                return False
    else:
        for i in range(len(pattern[0])):
            pattern_line = [p[i] for p in pattern]
            if not validate_pattern_line(pattern_line[start:end]):
                return False
    return True

def process_pattern(pattern: str):
    pattern = pattern.splitlines()
    horizontal = pattern[0]
    vertical = ''.join([p[0] for p in pattern])

    for i in range(len(horizontal)-1):
        if horizontal[0] == horizontal[-1-i]:
            if validate_pattern_line(horizontal[0:-i+len(horizontal)]):
                if validate_pattern(pattern, 0, -i+len(horizontal), True):
                    return (-i+len(horizontal))//2
                
        if horizontal[-1] == horizontal[i]:
            if validate_pattern_line(horizontal[i:]):
                if validate_pattern(pattern, i, len(horizontal), True):
                    return len(horizontal) - (-i+len(horizontal))//2

    for i in range(len(vertical)-1):
        if vertical[0] == vertical[-1-i]:
            if validate_pattern_line(vertical[0:-i+len(vertical)]):
                if validate_pattern(pattern, 0, -i+len(vertical), False):
                    return 100 * (-i+len(vertical))//2

        if vertical[-1] == vertical[i]:
            if validate_pattern_line(vertical[i:]):
                if validate_pattern(pattern, i, len(vertical), False):
                    return 100 * (len(vertical) - (-i+len(vertical))//2)
                
patterns = load_input().split('\n\n')
patterns_sum = 0
for pattern in patterns:
    patterns_sum += process_pattern(pattern)

print("Result 1:", patterns_sum)

# PART II

def validate_pattern_line_smudge(pattern_line: str) -> int:
    diff = 0
    for i in range(len(pattern_line)//2):
        if pattern_line[i] != pattern_line[-1-i]:
            diff += 1
    return diff

def validate_pattern_smudge(pattern: list[str], start: int, end: int, is_horizontal: bool) -> bool:
    diff = 0
    if is_horizontal:
        for pattern_line in pattern:
            diff += validate_pattern_line_smudge(pattern_line[start:end])
    else:
        for i in range(len(pattern[0])):
            pattern_line = [p[i] for p in pattern]
            diff += validate_pattern_line_smudge(pattern_line[start:end])
    return diff == 1

def process_pattern_smudge(pattern: str):
    pattern = pattern.splitlines()
    horizontal = pattern[0]
    vertical = ''.join([p[0] for p in pattern])

    for i in range(len(horizontal)-1):
        if horizontal[0] == horizontal[-1-i]:
            if validate_pattern_line_smudge(horizontal[0:-i+len(horizontal)]) <= 1:
                if validate_pattern_smudge(pattern, 0, -i+len(horizontal), True):
                    return (-i+len(horizontal))//2
                
        if horizontal[-1] == horizontal[i]:
            if validate_pattern_line_smudge(horizontal[i:]) <= 1:
                if validate_pattern_smudge(pattern, i, len(horizontal), True):
                    return len(horizontal) - (-i+len(horizontal))//2

    for i in range(len(vertical)-1):
        if vertical[0] == vertical[-1-i]:
            if validate_pattern_line_smudge(vertical[0:-i+len(vertical)]) <= 1:
                if validate_pattern_smudge(pattern, 0, -i+len(vertical), False):
                    return 100 * (-i+len(vertical))//2

        if vertical[-1] == vertical[i]:
            if validate_pattern_line_smudge(vertical[i:]) <= 1:
                if validate_pattern_smudge(pattern, i, len(vertical), False):
                    return 100 * (len(vertical) - (-i+len(vertical))//2)
                
patterns = load_input().split('\n\n')
patterns_sum = 0
for pattern in patterns:
    patterns_sum += process_pattern_smudge(pattern)

print("Result 2:", patterns_sum)