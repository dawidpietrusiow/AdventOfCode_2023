import functools

with open('input') as data:
    games = data.read().split('\n')

limits = {'red': 12, 'green': 13, 'blue': 14}

totalVal1 = 0
totalVal2 = 0

for i, game in enumerate(games):
    isPossible = True
    game = game[game.index(':') + 2:]
    rounds = game.split(';')

    lowest_possible = {'red':None, 'green':None, 'blue':None}
    for round in rounds:
        round = round.strip()
        cases = round.split(',')
        for case in cases:
            case = case.strip().split(' ')
            if int(case[0]) > limits[case[1]]:
                isPossible = False
            if lowest_possible[case[1]] is None or int(case[0]) > lowest_possible[case[1]]:
                lowest_possible[case[1]] = int(case[0])
    if isPossible:
        #Game num starts at 1, index at 0
        totalVal1 += i + 1

    totalVal2 += functools.reduce(lambda x,y: x * y, lowest_possible.values())

print(f'Part 1: {totalVal1}')
print(f'Part 2: {totalVal2}')

