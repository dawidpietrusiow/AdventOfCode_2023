class Cogwheel:
    def __init__(self, row, col):
        self.r = row
        self.c = col
        self.associated_nums = []

def checkChar(row, col, num):
    char = lines[row][col]

    if not char.isnumeric() and char != '.':
        if char == '*':
            for i in cogwheels:
                if i.r == row and i.c == col:
                    i.associated_nums.append(num)
        return True
    else:
        return False

def checkIfAdjacentChar(num, row, col):
    valid_num = False

    is_top = row == 0
    is_left = col == 0
    is_right = col + len(str(num)) == len(lines[row])
    is_bottom = row == len(lines) - 1

    start_col = col - 1 if not is_left else col
    end_col = col + len(str(num))+ 1 if not is_right else col + len(str(num))

    for c in range(start_col, end_col):
        #check row above
        if not is_top:
            if checkChar(row=row-1, col=c, num=num):
                valid_num = True

        #check row below
        if not is_bottom:
            if checkChar(row=row+1, col=c, num=num):
                valid_num = True

        #check inline row
        if checkChar(row=row, col=c, num=num):
            valid_num = True

    return valid_num

totalVal1 = 0
totalVal2 = 0
cogwheels = []

with open('machine_parts_scheme') as f:
    lines = f.read().split('\n')

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '*':
            cogwheels.append(Cogwheel(row=row, col=col))

for row, line in enumerate(lines):
    col = 0
    while col < len(line):
        if line[col].isnumeric():
            for end_col in range(len(line), col, -1):
                if (num := line[col:end_col]).isnumeric():
                    num = int(num)
                    if checkIfAdjacentChar(num=num, row=row, col=col):
                        totalVal1 += num
                    col = end_col-1
                    break
        col += 1

for i in cogwheels:
    if len(i.associated_nums) == 2:
        totalVal2 += (i.associated_nums[0] * i.associated_nums[1])

print(f'Part 1: {totalVal1}')
print(f'Part 2: {totalVal2}')

