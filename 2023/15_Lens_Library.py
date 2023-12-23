from input_utils import load_input

# PART I

class HolidayAsciiStringHelper:
    def __init__(self) -> None:
        self._current_value = 0

    def hash_character(self, character: str) -> int:
        self._current_value += ord(character)
        self._current_value *= 17
        self._current_value %= 256

    def hash_step(self, step: str) -> int:
        for char in step:
            self.hash_character(char)
        
    @property
    def current_value(self):
        return self._current_value

strings = load_input().splitlines()

hash_sum = 0
for strings_line in strings:
    for step in strings_line.split(','):
        holiday_ascii_string_helper = HolidayAsciiStringHelper()
        holiday_ascii_string_helper.hash_step(step)
        hash_sum += holiday_ascii_string_helper.current_value

print("Result 1:", hash_sum)

# PART II

class HolidayAsciiStringHelperManualArrangementProcedure:
    def __init__(self) -> None:
        self._boxes = [[] for i in range(256)]

    def parse_step(self, step: str) -> list[str]:
        for sign in ['-', '=']:
            if sign in step:
                step_parsed = step.split(sign)
                step_parsed.insert(1, sign)
                return [s for s in step_parsed if s]
            
    def process_step(self, step_parsed: list[str]) -> None:
        holiday_ascii_string_helper = HolidayAsciiStringHelper()
        holiday_ascii_string_helper.hash_step(step_parsed[0])
        hash_value = holiday_ascii_string_helper.current_value
        if step_parsed[1] == '=':
            self.add_lens(step_parsed[0], hash_value, step_parsed[2])
        elif step_parsed[1] == '-':
            self.remove_lens(step_parsed[0], hash_value)

    def add_lens(self, label: str, box_number: int, focal_length: int) -> None:
        box = [l if l[0] != label else 'x' for l in self._boxes[box_number]]
        if 'x' in box:
            box[box.index('x')] = (label, focal_length)
        else:
            box.append((label, focal_length))
        self._boxes[box_number] = box

    def remove_lens(self, label: str, box_number: int) -> None:
        box = [l for l in self._boxes[box_number] if l[0] != label]
        self._boxes[box_number] = box

    def print_boxes(self) -> None:
        for i, box in enumerate(self._boxes):
            print(i, box)
            if i >10: break
            
    def calculate_boxes(self) -> int:
        lens_sum = 0
        for b, box in enumerate(self._boxes):
            for l, lens in enumerate(box):
                lens_sum += (b + 1) * (l + 1) * int(lens[1])
        return lens_sum

hashmap = HolidayAsciiStringHelperManualArrangementProcedure()
for strings_line in strings:
    for step in strings_line.split(','):
        hashmap.process_step(hashmap.parse_step(step))
        
print("Result 2:", hashmap.calculate_boxes())