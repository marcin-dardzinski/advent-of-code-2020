import itertools

class Map:   
    def __init__(self, active: set, dims: int):
        self.active = active
        self.dims = dims

    def bounds(self):
        def swap(idx, axis, value, f):
            minmax[idx][axis] = f(value, minmax[idx][axis])

        minmax = [[1000000000] * self.dims, [-1000000000] * self.dims]

        for coord in self.active:
            for axis, value in enumerate(coord):
                swap(0, axis, value, min)
                swap(1, axis, value, max)

        return tuple(minmax[0]), tuple(minmax[1])

    def get(self, coord):
        return '#' if coord in self.active else '.'

    def set(self, coord, value):
        if value == '#':
            self.active.add(coord)
        else: 
            self.active.discard(coord)

    def count_neighbors(self, coord):
        def rng(axis): 
            return range(coord[axis]-1, coord[axis]+2)

        c = 0
        for n in itertools.product(*[rng(i) for i,_ in enumerate(coord)]):
            if n != coord and self.get(n) == '#':
                c += 1
        return c

    def clone(self):
        return Map(self.active.copy(), self.dims)

    @staticmethod
    def init(grid: str, dims: int):
        active = set()

        grid = grid.splitlines()
        suffix = [0] * (dims - 2)

        y = len(grid)
        x = len(grid[0])

        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if value == '#':
                    active.add((x,y,*suffix))
        
        return Map(active, dims)


    @staticmethod
    def simulate(grid, rounds, dims):
        map = Map.init(grid, dims)

        for _ in range(rounds):
            clone = map.clone()
            min, max = map.bounds()

            def rng(axis):
                return range(min[axis]- 1, max[axis] + 2)
  
            for coord in itertools.product(*[rng(i) for i in range(map.dims)]):
                v = map.get(coord)
                n = map.count_neighbors(coord)

                if v == '#' and (n < 2 or n > 3):
                    clone.set(coord, '.')
                elif v == '.' and n == 3:
                    clone.set(coord, '#')

            map = clone

        return len(map.active)


input = """.#.
..#
###"""

with open('input.txt') as file:
    input = file.read()

print(Map.simulate(input, 6, 4))