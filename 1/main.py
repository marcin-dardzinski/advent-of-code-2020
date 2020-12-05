def sum_year(xs):
    s = set(xs)

    for x in xs:
        diff = 2020 - x
        if diff in s:
            return x, diff
    return None


def sum_year2(xs):
    xs = sorted(xs)


arr = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

# print(sum_year(arr))

with open('input.txt', 'r') as file:
    arr = [int(x) for x in file.readlines()]
    x, y = sum_year(arr)
    print(x * y)
