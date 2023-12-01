from input_utils import load_input
import string

input_data = load_input()

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def find_digit(line, index):
    if line[index] in string.digits:
        return int(line[index])
    for k, v in digits.items():
        if line[index:].startswith(k):
            return v
    return False

calibration = 0
for input_line in input_data.splitlines():
    first = False
    last = False
    for i in range(len(input_line)):
        if not first:
            if find_digit(input_line, i):
                calibration += 10 * find_digit(input_line, i)
                f = find_digit(input_line, i)
                first = True

        if not last:
            if find_digit(input_line, -i-1):
                calibration += find_digit(input_line, -i-1)
                l = find_digit(input_line, -i-1)
                last = True
            
    #print(f"{input_line} -> {f}{l}")
print(calibration)