with open('input') as input:
    input_text = input.read()

list = input_text.split('\n')

seeds = list[0][list[0].find(':') + 1:].strip().split(' ')
list.pop(0)
for el in list:
    if el == '':
        list.remove('')

index = 0
maps = []
while index < len(list):
    if 'map:' in list[index]:
        maps.append([])
    else: maps[-1].append(list[index].split(' '))
    index += 1

print(seeds)
print(maps)
