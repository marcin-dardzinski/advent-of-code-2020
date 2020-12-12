import math

def rotate(x,y, degree):
    s = round(math.sin(degree/360 * 2 * math.pi))
    c = round(math.cos(degree/360 * 2 * math.pi))

    return x * c - y * s, x * s + y * c

def simulate(actions):
    x,y = 0,0
    dx, dy = 1,0
    
    for a in actions:
        action, value = a[0], int(a[1:])

        if action == 'N':
            y += value
        elif action == 'E':
            x += value
        elif action == 'S':
            y -= value
        elif action == 'W':
            x -= value
        elif action == 'F':
            x += value * dx
            y += value * dy
        elif action == 'R':
            dx, dy = rotate(dx, dy, -value)
        elif action == 'L':
            dx, dy = rotate(dx, dy, value)
        else:
            raise RuntimeError("unexpected value")
    return abs(x) + abs(y)


def simulate2(actions):
    x,y = 0,0
    wx, wy = 10, 1
    
    for a in actions:
        action, value = a[0], int(a[1:])

        if action == 'N':
            wy += value
        elif action == 'E':
            wx += value
        elif action == 'S':
            wy -= value
        elif action == 'W':
            wx -= value
        elif action == 'F':
            x += value * wx
            y += value * wy
        elif action == 'R':
            wx, wy = rotate(wx,wy, -value)
        elif action == 'L':
            wx, wy = rotate(wx,wy, value)
        else:
            raise RuntimeError("unexpected value")
    return abs(x) + abs(y)




input = """F10
N3
F7
R90
F11""".splitlines()

with open('input.txt') as file:
    input = file.read().splitlines()

print(simulate(input))
print(simulate2(input))