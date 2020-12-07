def count_group(gr: str):
    return len(set(gr.replace('\n', '')))


def count_group2(gr: str):
    lines = gr.split()
    ans = set(lines[0])
    l = len(ans)

    for x in lines[1:]:
        ans.intersection_update(x)
        if len(ans) == 0:
            return 0
    return len(ans)


def count_all(all: str, f):
    groups = all.split('\n\n')
    return sum(map(f, groups))


input = """abc

a
b
c

ab
ac

a
a
a
a

b"""

with open('input.txt') as file:
    input = file.read()

print(count_all(input, count_group))
print(count_all(input, count_group2))
