import numpy as np

def count_adjacent(x,y,seats):
    taken = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if  j >= 0 and j < len(seats) and i >= 0 and i < len(seats[j]) and (x,y) != (i,j) and seats[j][i] == '#':
                taken += 1
    return taken

def count_adjacent2(x,y, seats):
    x_max, y_max = seats.shape 

    def visible(x_diff, y_diff):
        i,j = x + x_diff, y + y_diff
        while i >= 0 and i < x_max and j >= 0 and j < y_max:
            seat = seats[j, i]
            if seat == '#':
                return 1
            elif seat == 'L':
                return 0
            i,j = i + x_diff, j + y_diff
        return 0
    
    return visible(-1, 1) + \
        visible(0, 1) + \
        visible(1, 1) + \
        visible(-1, 0) + \
        visible(1, 0) + \
        visible(-1, -1) + \
        visible(0, -1) +\
        visible(1, -1)
           


def comp(x, y):
    for i in range(len(x)):
        for j in range (len(x[i])):
            if x[i][j] != y[i][j]:
                return False
    return True

def count(seats):
    c = 0
    for row in seats:
        for x in row:
            if x == '#':
                c += 1
    return c

def simulate(seats: np.ndarray):
    while True:
        clone = np.copy(seats)

        for (y,x), seat in np.ndenumerate(seats):
                if seat == 'L' and count_adjacent2(x,y,seats) == 0:
                    clone[y,x] = '#'
                elif seat == '#' and count_adjacent2(x,y, seats) >= 5:
                    clone[y,x] = 'L'
        
        if np.array_equal(clone, seats):
            break

        seats = clone
    
    return np.count_nonzero(seats == '#')
                


input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()

# with open('input.txt') as file:
#     input = file.read().splitlines()

input = np.array(input)
input = input.view('U1').reshape((input.size, -1))

print(simulate(input))




