with open('AOC_day1_data.txt') as data:
    games = data.read().split('\n')

limits = {'red': 12, 'green': 13, 'blue': 14}

totalVal = 0
hej = 1

for i, game in enumerate(games):
    isPossible = True
    game = game[game.index(':') + 2:]
    rounds = game.split(';')
    for round in rounds:
        round = round.strip()
        cases = round.split(',')
        for case in cases:
            case = case.strip().split(' ')
            if int(case[0]) > limits[case[1]]:
                isPossible = False
    if isPossible:
        #Game num starts at 1, index at 0
        totalVal += i + 1

print(totalVal)

