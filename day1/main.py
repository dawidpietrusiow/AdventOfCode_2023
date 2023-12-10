try:
    with open("data") as data:
        lines = data.readlines()
except FileNotFoundError as e:
    print(e)
else:

    totalVal1 = 0
    totalVal2 = 0

    numsInText = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for line in lines:
        numsInLine1 = []
        numsInLine2 = []
        for i, char in enumerate(line):
            if char.isnumeric():
                numsInLine1.append(char)
                numsInLine2.append(char)
            for j, num in enumerate(numsInText):
                if line[i:].startswith(num):
                    numsInLine2.append(str(j))
        combinedVal1 = int(numsInLine1[0] + numsInLine1[-1])
        combinedVal2 = int(numsInLine2[0] + numsInLine2[-1])
        totalVal1 += combinedVal1
        totalVal2 += combinedVal2

    print("Pt1: {pt1}\nPt2: {pt2}".format(pt1=str(totalVal1), pt2=str(totalVal2)))