def diffs(joltages: list):
    joltages.append(0)
    joltages.append(max(joltages) + 3)
    joltages.sort()

    diffs = zip(joltages, joltages[1:])
    # groups = dict()
    ones, threes = 0,0

    for low,high in diffs:
        diff = high - low
        if diff == 1:
            ones += 1
        elif diff == 2:
            pass
        elif diff == 3:
            threes += 1
        else:
            raise RuntimeError("unexpected")

    return ones * threes

def combinations(joltages):
    joltages.append(0)
    joltages.append(max(joltages) + 3)
    joltages.sort()

    opts = [0] * len(joltages)
    opts[-1] = 1

    def check_idx(x, i, target):
        if target < len(joltages) and joltages[target] - x <= 3:
            opts[i] += opts[target]

    for i in reversed(range(len(joltages)- 1)):
        x = joltages[i]
        check_idx(x, i, i + 1)
        check_idx(x, i, i + 2)
        check_idx(x, i, i + 3)

    return opts[0]
        

input = [int(x) for x in """16
10
15
5
1
11
7
19
6
12
4""".splitlines()]


input = [ int(x) for x in """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines()]

with open('input.txt') as file:
    input = [int(x) for x in file.readlines()]

# print(diffs(input))
print(combinations(input))