# Advent of Code Day 3: Rucksack Reorganization

from functools import reduce
f = open('2022/Day03/Day3.txt', 'r')
data = f.read().split('\n')
values = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
listOfCompartments = list(map(lambda x: [x[0:int(len(x)/2)], x[int(len(x)/2):]], data))

priorities = []
for i in range(len(listOfCompartments)):
  for j in listOfCompartments[i][0]:
    if j in listOfCompartments[i][1]:
      priorities.append(values.find(j))
      break

sumOfPriorities = reduce(lambda x, y: x+y, priorities)
print(f'The sum of the priorities of the item type that appears in both compartments of each rucksack is {sumOfPriorities}')

# Part 2
listOfGroups = []
rows = 3
while rows <= len(data):
  listOfGroups.append(data[rows-3:rows])
  rows += 3

priorities2 = []
for i in range(len(listOfGroups)):
  for j in listOfGroups[i][0]:
    if j in listOfGroups[i][1] and j in listOfGroups[i][2]:
      priorities2.append(values.find(j))
      break

sumOfPriorities2 = reduce(lambda x, y: x+y, priorities2)
print(f'The sum of the priorities of the item type that corresponds to the badges of each three-Elf group is {sumOfPriorities2}')
