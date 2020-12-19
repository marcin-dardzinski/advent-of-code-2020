import re
import math

is_int = re.compile('\d+')

def calc(op, a, b):
    return a + b if op == '+' else a*b

def tokenize(input: str):
    idx = 0
    while idx < len(input):
        while input[idx] == ' ':
            idx += 1

        c = input[idx]
        if c in ['+', '*', '(', ')']:
            idx += 1
            yield c
        else:
            x = is_int.match(input, idx)[0]
            idx += len(x)
            yield int(x)



def part_one(input: str):
    tokens = list(tokenize(input))
    idx = 0
    def calc_no_paren():
        nonlocal idx
        val = None
        op = None
        while idx < len(tokens):
            token = tokens[idx]
            idx += 1
            if token == '(':
                x = calc_no_paren()
                if val is None:
                    val = x
                else:
                    val = calc(op, val, x)
            elif token == ')':
                return val
            elif token in ['*', '+']:
                op = token
            else:
                if val is None:
                    val = token
                else:
                    val = calc(op, val, token)
        return val
    
    return calc_no_paren()

def part_two(input: str):
    tokens = list(tokenize(input))
    idx = 0
    def calc_no_paren():
        nonlocal idx
        vals = []
        op = None
        while idx < len(tokens):
            token = tokens[idx]
            idx += 1
            if token == '(':
                x = calc_no_paren()
                if op == '+':
                    vals[-1] = vals[-1] + x
                else:
                    vals.append(x)
            elif token == ')':
                return math.prod(vals)
            elif token in ['*', '+']:
                op = token
            else:
                if op == '+':
                    vals[-1] = vals[-1] + token
                else:
                    vals.append(token)
        return math.prod(vals)
    
    return calc_no_paren()
       
    # stack = []
    # for x in tokenize(input):
    #     if isinstance(x, int):
    #         if len(stack) > 0 and stack[-1] in ['+', '*']:
    #             op = stack.pop()
    #             a = stack.pop() 
    #             stack.append(calc(op, a, x))
    #         else:
    #             stack.append(x)
    #     elif x != ')':
    #         stack.append(x)
    #     elif len(stack) > 1:
    #         val = stack.pop()
    #         stack.pop()
    #         while len(stack) > 0 and stack[-1] in ['*', '+']:
    #             op = stack.pop()
    #             a = stack.pop() 
    #             val = calc(op, a, val)
    #             if len(stack) > 0 and stack[-1] == '(':
    #                 stack.pop()
    #         stack.append(val)
    
    # assert len(stack) == 1
    # return stack[0]

# print(part_one('1 + 2 * 3 + 4 * 5 + 6'))
# print(part_one('1 + (2 * 3) + (4 * (5 + 6))'))
# print(part_one('2 * 3 + (4 * 5)'))
# print(part_one('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
# print(part_one('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
# print(part_one('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))   

print(part_two('1 + 2 * 3 + 4 * 5 + 6'))
print(part_two('1 + (2 * 3) + (4 * (5 + 6))'))
print(part_two('2 * 3 + (4 * 5)'))
print(part_two('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
print(part_two('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
print(part_two('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))   


with open('input.txt') as file:
    calcs = file.read().splitlines()
    print(sum(map(part_one, calcs)))
    print(sum(map(part_two, calcs)))