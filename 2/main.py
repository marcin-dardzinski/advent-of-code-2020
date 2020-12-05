def split(line: str):
    lens, chr, psswd = line.split()

    min, max = lens.split('-')
    min, max = int(min), int(max)
    chr = chr[0]
    return min, max, chr, psswd


def valid(line: str):
    min, max, chr, psswd = split(line)

    count = len(list(filter(lambda x: x == chr, psswd)))
    return count >= min and count <= max


def valid2(line: str):
    fst, scd, chr, psswd = split(line)

    fst = psswd[fst - 1]
    scd = psswd[scd - 1]

    return (fst == chr) ^ (scd == chr)


with open('input.txt', 'r') as file:
    lines = file.readlines()

print(len(list(filter(valid2, lines))))
