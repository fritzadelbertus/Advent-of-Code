# Advent of Code Day 11: Monkey in the Middle Part 2
import re

f = open('2022/Day11/Day11.txt', 'r')
data = f.read().split('\n\n')

def generateOperation(strOp):
  ops = strOp.split(' ')
  if ops [2] == '*':
    return [ops[3], 'multiplication']
  if ops [2] == '+':
    return [ops[3], 'addition']

commonDivisor = 1

monkeys2 = []
for rawMonkey in data:
  monkeyInfo = rawMonkey.split('\n')
  monkeyNumber = re.search(r'\d+', monkeyInfo[0]).group()
  items = re.findall(r'\d+',monkeyInfo[1])
  items = list(map(lambda x: int(x), items))
  operation = monkeyInfo[2].split('=')[-1]
  divisilbleTest = re.search(r'\d+', monkeyInfo[3]).group()
  tMonkey = re.search(r'\d+', monkeyInfo[4]).group()
  fMonkey = re.search(r'\d+', monkeyInfo[5]).group()
  commonDivisor *= int(divisilbleTest)
  monkeyData = {
    'number': int(monkeyNumber),
    'items': items,
    'operation': generateOperation(operation),
    'test': int(divisilbleTest),
    'true': int(tMonkey),
    'false': int(fMonkey),
    'inspection': 0
  }

  monkeys2.append(monkeyData)

for monkey in monkeys2:
  for item in monkey['items']:
    itemLocation = monkey
    rounds = 10000
    i = 0
    while i < rounds:
      temp = itemLocation['number']
      itemLocation['inspection'] += 1
      if itemLocation['operation'][1] == 'multiplication':
        if itemLocation['operation'][0] != 'old':
          item = int(itemLocation['operation'][0]) * item
        else:
          item *= item
      elif itemLocation['operation'][1] == 'addition':
        item = int(itemLocation['operation'][0]) + item
      item = item % commonDivisor
      if item % itemLocation['test'] == 0:
        itemLocation = monkeys2[itemLocation['true']]
      else:
        itemLocation = monkeys2[itemLocation['false']]
      if temp < itemLocation['number']:
        i -= 1
      i += 1

max1 = 0
max2 = 0

for monkey in monkeys2:
  if monkey['inspection'] > max1:
    max2 = max1
    max1 = monkey['inspection']
  elif monkey['inspection'] > max2:
    max2 = monkey['inspection']

answer2 = max1 * max2
print(f'I had enough with the monkeys and finally the final answer for part 2 is {answer2}')
