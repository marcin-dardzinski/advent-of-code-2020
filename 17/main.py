import itertools

class Map:   
    def __init__(self, min, max, map):
        self.min = min
        self.max = max
        self.map = map

    def get(self, coord):
        return self.map.get(coord, '.')

    def set(self, coord, value):
        def swap(a, b, f):
            xa, ya, za = a
            xb, yb, zb = b
            return f(xa,xb), f(ya, yb), f(za, zb)
        
        self.min = swap(self.min, coord, min)
        self.max = swap(self.max, coord, max)
        self.map[coord] = value

    def count_neighbors(self, coord):
        def rng(axis): 
            return range(coord[axis]-1, coord[axis]+2)

        c = 0
        for n in itertools.product(rng(0), rng(1), rng(2)):
            if n != coord and self.get(n) == '#':
                c += 1
        return c

    def dump(self):
        def rng(axis):
            return range(self.min[axis], self.max[axis] + 1)

        for z in rng(2):
            for y in rng(1):
                line = ''.join([ self.map.get((x,y,z)) for x in rng(0)])
                print(line)

            print()


    def clone(self):
        return Map(self.min, self.max, self.map.copy())

    @staticmethod
    def init(grid: str):
        map = dict()

        grid = grid.splitlines()

        y = len(grid)
        x = len(grid[0])
        min = (0, 0, 0)
        max = (x - 1, y - 1, 0)

        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                map[(x,y,0)] = value
        
        return Map(min, max, map)


    @staticmethod
    def simulate(grid, rounds):
        def rng(axis):
            return range(map.min[axis]- 1, map.max[axis] + 2)
        
        map = Map.init(grid)

        for _ in range(rounds):
            clone = map.clone()
            for coord in itertools.product(rng(0), rng(1), rng(2)):
                v = map.get(coord)
                n = map.count_neighbors(coord)

                if v == '#' and (n < 2 or n > 3):
                    clone.set(coord, '.')
                elif v == '.' and n == 3:
                    clone.set(coord, '#')

            map = clone

        return len(list(filter(lambda x: x == '#', map.map.values())))


input = """.#.
..#
###"""

with open('input.txt') as file:
    input = file.read()

print(Map.simulate(input, 6))