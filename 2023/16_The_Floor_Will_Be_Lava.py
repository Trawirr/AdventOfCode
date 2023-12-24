from __future__ import annotations
from input_utils import load_input

# PART I

class Beam:
    def __init__(self, coords: list[int], direction: list[int]) -> None:
        self._coords = coords
        self._direction = direction

    def is_in_grid(self, size_x: int, size_y: int) -> bool:
        return 0 <= self._coords[0] < size_x and 0 <= self._coords[1] < size_y

    def move(self) -> None:
        self._coords = [self._coords[i] + self._direction[i] for i in range(2)]

    def change_direction(self, change_sign: bool = False) -> None:
        sign = -1 if change_sign else 1
        self._direction = [sign * self._direction[1], sign * self._direction[0]]

    def process_element(self, element: str) -> None | list[int]:
        if element in ['\\', '/']:
            self.process_dash(element)
        elif element in ['-', '|']:
            new_beam = self.process_splitter(element)
            if new_beam is not None:
                return new_beam
        return None

    def process_dash(self, dash: str) -> None:
        if dash == '\\':
            self.change_direction()
        elif dash == '/':
            self.change_direction(True)
        return None

    def process_splitter(self, splitter: str) -> None | Beam:
        if (self._direction[0] != 0 and splitter == '|') or (self._direction[1] != 0 and splitter == '-'):
            new_beam = Beam(self._coords, self._direction)
            new_beam.change_direction(True)
            self.change_direction()
            return new_beam
        return None

    @property
    def coords(self):
        return self._coords
    
    @property
    def coords_direction(self):
        return (self._coords, self._direction)

class Contraption:
    def __init__(self, grid: list[str], beam_coords: list[int] = [-1, 0], beam_direction: list[int] = [1, 0]) -> None:
        self._beams = [Beam(beam_coords, beam_direction)]
        self._grid = grid
        self._size_x = len(grid)
        self._size_y = len(grid[0])
        self._visited_elements = []
        self._visited_grid = [[0 for g in grid_line] for grid_line in grid]

    def get_element(self, coords: list[int]) -> str:
        x, y = coords
        return self._grid[y][x]
    
    def set_visited_grid(self) -> None:
        x, y = self._beams[0].coords
        self._visited_grid[y][x] = 1

    def calculate_visited_grid(self) -> int:
        return sum([sum(g) for g in self._visited_grid])
    
    def print_visited_grid(self) -> None:
        for g in self._visited_grid:
            print(g)

    def move_beam(self) -> bool:
        self._beams[0].move()
        if not self._beams[0].is_in_grid(self._size_x, self._size_y):
            self._beams.pop(0)
        else:
            self.set_visited_grid()
            element = self.get_element(self._beams[0].coords)
            if element != '.':
                if self._beams[0].coords_direction in self._visited_elements:
                    self._beams.pop(0)
                else:
                    self._visited_elements.append(self._beams[0].coords_direction)
                    new_beam = self._beams[0].process_element(element)
                    if new_beam is not None:
                        self._beams.append(new_beam)
        return len(self._beams) > 0

grid = load_input().splitlines()
contraption = Contraption(grid)
while contraption.move_beam():
    pass

print("Result 1:", contraption.calculate_visited_grid())

# PART II

max_visited = 0
for i in range(len(grid)):
    contraption = Contraption(grid, [-1, i], [1, 0])
    while contraption.move_beam():
        pass
    max_visited = max(max_visited, contraption.calculate_visited_grid())
    contraption = Contraption(grid, [len(grid[0]), i], [-1, 0])
    while contraption.move_beam():
        pass
    max_visited = max(max_visited, contraption.calculate_visited_grid())


for i in range(len(grid[0])):
    contraption = Contraption(grid, [i, -1], [0, 1])
    while contraption.move_beam():
        pass
    max_visited = max(max_visited, contraption.calculate_visited_grid())
    contraption = Contraption(grid, [i, len(grid)], [0, -1])
    while contraption.move_beam():
        pass
    max_visited = max(max_visited, contraption.calculate_visited_grid())

print("Result 2:", max_visited)