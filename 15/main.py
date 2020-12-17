def simulate(numbers: list[int], max_round):
    spoken = dict()
    round = 1
    for x in numbers:
        spoken[x] = [round]
        round += 1
    
    last = numbers[-1]

    while round <= max_round:
        spoken_before = spoken[last]
        if len(spoken_before) > 1:
            curr = spoken_before[-1] - spoken_before[-2]
        else:
            curr = 0
            
        spoken.setdefault(curr, []).append(round)
        last = curr
        round += 1

    return last


input = [7,12,1,0,16,2]

print(simulate(input, 2020))
print(simulate(input, 30000000))