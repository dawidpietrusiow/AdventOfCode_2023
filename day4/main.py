import math


class Card:
    def __init__(self, card_index, winning_nums, playing_nums):
        self.card_amount = 1

        self.card_index = card_index
        self.winning_nums = winning_nums
        self.playing_nums = playing_nums
        self.matches = self.gather_matches()
        self.score = self.calc_score()

    def gather_matches(self):
        matches = 0
        for i in self.playing_nums:
            for j in self.winning_nums:
                if i == j:
                    matches += 1
        return matches

    def calc_score(self):
        if self.matches == 0:
            score = 0
        else:
            score = math.pow(2, self.matches - 1)
        return int(score)

cards = []
totalValue1 = 0
totalValue2 = 0

with open('input') as input:
    lines = input.read().split('\n')

for card_index, line in enumerate(lines):
    line = line[(line.find(':') + 2):].split('|')

    winning_line = line[0].strip()
    playing_line = line[1].strip()

    winning_nums = winning_line.replace('  ', ' ').split(' ')
    playing_nums = playing_line.replace('  ', ' ').split(' ')


    cards.append(Card(card_index=card_index, playing_nums=playing_nums, winning_nums=winning_nums))

for card in cards:
    totalValue1 += card.score


for card in cards:
    for i in range(card.card_index + 1, card.card_index + 1 + card.matches):
        if i > len(cards):
            break
        target_copy_card = cards[i]
        target_copy_card.card_amount += card.card_amount

for card in cards:
    totalValue2 += card.card_amount

print('Part 1: ' + str(totalValue1))
print('Part 2: ' + str(totalValue2))