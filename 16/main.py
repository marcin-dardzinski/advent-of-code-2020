import re
import itertools

r = re.compile('\d+')

def parse_value(rule: str):
    v = r.findall(rule)
    return int(v[0]), int(v[1])


def parse_rules(rules: str):
    lines = rules.splitlines()

    rules = {}

    for line in lines:
        name, values = line.split(':')
        values = values.split('or')
        values = [parse_value(v) for v in values]

        rules[name] = values
    return rules

def parse_ticket(ticket: str):
    ticket = ticket.split(',')
    return [int(x) for x in ticket]

def validate_single(x: int, rules: list[int,int]):
    for low,high in rules:
        if x >= low and x <= high:
            return True
    return False

def validate_field(x: int, rules: dict):
    for low, high in itertools.chain.from_iterable(rules.values()):
        if x >= low and x <= high:
            return True
    return False

def validate_ticket(ticket: list[int], rules: dict):
    for x in ticket:
        if not validate_field(x, rules):
            return False
    return True


def part_one(input: str):
    input = input.split('\n\n')
    rules, tickets = input[0], input[2]
    rules = parse_rules(rules)
    tickets = [parse_ticket(t) for t in tickets.splitlines()[1:]]

    sum = 0
    for t in itertools.chain.from_iterable(tickets):
        if not validate_field(t, rules):
            sum += t
    return sum

def find_single_field(field: str, candidates: list[set]):
    idx = None
    for i, c in enumerate(candidates):
        if field in c:
            if idx is None:
                idx = i
            else:
                return None
    return idx


def part_two(input: str):
    rules, my_ticket, tickets = input.split('\n\n')
    rules = parse_rules(rules)
    tickets = [parse_ticket(t) for t in tickets.splitlines()[1:]]
    my_ticket = parse_ticket(my_ticket.splitlines()[1])

    tickets = list(filter(lambda x: validate_ticket(x, rules), tickets))

    candidate_fields = [set(rules.keys()) for _ in tickets[0]]

    for ticket in tickets:
        for i, field in enumerate(ticket):
            for rule in list(candidate_fields[i]):
                if not validate_single(field, rules[rule]):
                    candidate_fields[i].remove(rule)

    not_matched = set(rules.keys())

    while len(not_matched) > 0:
        for f in list(not_matched):
            idx = find_single_field(f, candidate_fields)
            if idx is not None:
                candidate_fields[idx].intersection_update([f])
                for i, fs in enumerate(candidate_fields):
                    if i != idx and f in fs:
                        fs.remove(f)
                not_matched.remove(f)

    field_names = [s.pop() for s in candidate_fields]
    prod = 1
    for i, field in enumerate(field_names):
        if field.startswith('departure'):
            prod *= my_ticket[i]


    return prod




input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

with open('input.txt') as file:
    input = file.read()

# print(part_one(input))
print(part_two(input))