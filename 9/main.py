def can_construct(n, window):
    for i,x in enumerate(window):
        for y in window[i+1:]:
            if x != y and x + y == n:
                return True
    return False


def find_sum(n, xs):
    start, end = 0, 1
    sum = xs[0]

    while True:
        if end >= len(xs):
            raise RuntimeError("cannot find the sequence")
        
        if sum > n:
            sum -= xs[start]
            start += 1
            if end == start:
                end + 1
        elif sum < n:
            sum += xs[end]
            end += 1
        else:
            rng = xs[start:end]
            return min(rng) + max(rng)


        




def decode(ns,  window_size):

    for i, x in enumerate(ns[window_size:]):
        window = ns[i:i + window_size]
        if not can_construct(x, window):
            return x, find_sum(x, ns[:i])

    raise RuntimeError("no match")

input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()


with open('input.txt') as file:
    input = file.read().splitlines()

input = [int(x) for x in input]

print(decode(input, 25))






