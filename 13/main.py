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


def part_two(lines):
    base = lines[0]
    for i,x in enumerate(lines):
        if x != 0:
            print('{}n + {} = {}n_{},'.format(base, i, x , i))

    # just copy it to Wolfram and solve over integers :)

def verify(input, solution):
    z = input[0]
    solution = z * solution
    print(solution)
    for i,x in enumerate(input):
        if x != 0:
            print((solution + i)/ x)

# print(earliest(939, np.array([7,13,59,31,19])))
# print(earliest(1000052, np.array([23,37,863,19,13,17,29,571,41])))


# part_two([7,13,0,0,59,0,31,19])
input = [23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,37,0,0,0,0,0,863,0,0,0,0,0,0,0,0,0,0,0,19,13,0,0,0,17,0,0,0,0,0,0,0,0,0,0,0,29,0,571,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41]
part_two(input)
verify(input, 577373815998)