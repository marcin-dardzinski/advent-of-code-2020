import numpy as np

def earliest(time, lines):
    nearest = lines * np.ceil(time / lines)
    min = np.argmin(nearest)

    wait = nearest[min] - time
    return wait * lines[min]

def check_match(time, lines):
    for i,x in enumerate(lines):
        if x == 0:
            continue
        if time + 1 % x != 0:
            return False
    return True    


def brute(lines):
    x = lines[0]

    while not check_match(x, lines):
        x += lines[0]

    return x


# print(earliest(939, np.array([7,13,59,31,19])))
# print(earliest(1000052, np.array([23,37,863,19,13,17,29,571,41])))

print(brute([7,13,0,0,59,0,31,19]))
