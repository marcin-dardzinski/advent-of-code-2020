from queue import SimpleQueue

def parse(s: str):
    s = s.split('contain')
    parent = ' '.join(s[0].split()[:2])

    childrenStr = s[1]
    if "no other bags" in childrenStr:
        return parent, []
    
    children = childrenStr.split(',')
    parsed = []
    for x in children:
        x = x.split()
        name = ' '.join(x[1:3])
        count = int(x[0])
        parsed.append((name, count))
        
    return parent, parsed


def make_graph(lines: str):
    parents = dict()
    for line in lines:
        parent, children = parse(line)
        for child, _ in children:
            ps = parents.setdefault(child, set())
            ps.add(parent)
    return parents

def traverse(g: dict, start: str):
    visited = set()
    q = SimpleQueue()
    q.put(start)

    while not q.empty():
        i = q.get()
        visited.add(i)
        for n in g.get(i, []):
            if n not in visited:
                q.put(n)
    return len(visited) - 1

def make_graph2(lines: str):
    parents = dict()
    for line in lines:
        parent, children = parse(line)
        parents[parent] = children
    return parents

def traverse2(graph: dict, node: str):
    children = [count * traverse2(graph, name) for name, count in graph.get(node, [])]
    return 1 + sum(children)



input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()


# with open('input.txt') as file:
#     input = file.readlines()

g1 = make_graph(input)
g2 = make_graph2(input)

print(traverse(g1, 'shiny gold'))
print(traverse2(g2, 'shiny gold'))
