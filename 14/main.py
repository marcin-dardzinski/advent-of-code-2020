import re

r = re.compile('\d+')

def parse_cmd(cmd: str):
    match = r.findall(cmd)
    return int(match[0]), int(match[1])



def apply(cmds: list[str]):
    mem = dict()
    for cmd in cmds:
        if cmd.startswith('mask = '):
            mask = cmd.removeprefix('mask = ')
            and_mask = int(mask.replace('X', '1'),2)
            or_mask = int(mask.replace('X', '0'), 2)

        else:
            addr, value = parse_cmd(cmd)
            value = (value & and_mask) | or_mask
            mem[addr] = value
    
    return sum(mem.values())


def float_addr(addr, mask):
    l = len(mask)
    indices = [l - i - 1 for i, x in enumerate(mask) if x == "X"]

    addrs = []
    
    def gen(i, value):
        if i == len(indices):
            addrs.append(value)
            return
        
        one = value | 1 << indices[i]
        gen(i+1, one)
        zero = value & ~(1 << indices[i])
        gen(i+1, zero)
    
    gen(0, addr)
    return addrs

def part2(cmds: list[str]):
    mem = dict()
    for cmd in cmds:
        if cmd.startswith('mask = '):
            mask = cmd.removeprefix('mask = ')
            or_mask = int(mask.replace('X', '0'), 2)

        else:
            addr, value = parse_cmd(cmd)
            addr = addr | or_mask

            for addr in float_addr(addr, mask):
                mem[addr] = value
    
    return sum(mem.values())



input= """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".splitlines()

input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".splitlines()

with open('input.txt') as file:
    input = file.read().splitlines()
 
# print(apply(input))
print(part2(input))

