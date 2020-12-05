def parse(code: str):
    row = code[:7].replace('F', '0').replace('B', '1')
    col = code[-4:-1].replace('L', '0').replace('R', '1')

    row = int(row, 2)
    col = int(col, 2)
    return row * 8 + col


with open('input.txt') as file:
    codes = file.readlines()


codes = [parse(code) for code in codes]
print(max(codes))

codes = list(sorted(codes))

for x, y in zip(codes, codes[1:]):
    if y != x + 1:
        print(x+1)
