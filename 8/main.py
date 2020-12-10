def run(instructions):
    acc = 0
    executed = set()
    i = 0
    while True:
        if i in executed:
            return None
        if i >= len(instructions):
            return acc

        executed.add(i)
        op, value = instructions[i].split()
        value = int(value)

        if op == 'acc':
            acc += value
            i += 1
        elif op == 'jmp':
            i += value
        else:
            i += 1

    
def generate(instructions: list):
    for i,x in enumerate(instructions):
        op = x.split()[0]
        if op == 'jmp' or op == 'nop':
            new_op = 'nop' if op == 'jmp' else 'jmp'
            cp = instructions.copy()
            cp[i] = cp[i].replace(op, new_op)
            yield cp


input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1  
jmp -4 
acc +6""".splitlines()


with open('input.txt') as file:
    input = file.read().splitlines()

# print(run(input))

for x in generate(input):
    res = run(x)
    if res is not None:
        print(res)
        break