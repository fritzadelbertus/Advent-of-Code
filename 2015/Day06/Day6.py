# Advent of Code Day 6: Probably a Fire Hazard

import re
f = open('2015/Day06/Day6.txt', 'r')
raw = f.read().split('\n')
listOfInstructions = []
for i in raw:
  listOfInstructions.append(re.search(r'([A-Za-z ]+)(\d+),(\d+) through (\d+),(\d+)', i).groups())

def generateLightField(length):
  return [[0 for a in range(length)] for b in range(length)]

def countValue(lightField):
  return sum(map(lambda x: sum(x), lightField))

# Part 1
def switchLights(position, value, lightField):
  startOfRow, startOfCol, endOfRow, endOfCol = position
  if value == 'toggle ':
    for i in range(startOfRow, endOfRow+1):
      for j in range(startOfCol, endOfCol+1):
        lightField[i][j] = 1 if lightField[i][j] == 0 else 0
  else:
    if value == 'turn on ':
      change = 1
    elif value == 'turn off ':
      change = 0
    for i in range(startOfRow, endOfRow+1):
      for j in range(startOfCol, endOfCol+1):
        lightField[i][j] = change

lights1 = generateLightField(1000)

for i in listOfInstructions:
  position = [int(i[1]), int(i[2]), int(i[3]), int(i[4])]
  switchLights(position, i[0], lights1)

numLightsOn = countValue(lights1)
print(f'There are a total of {numLightsOn} which are turned on.')

# Part 2
def switchBrigthness(position, value, lightField):
  startOfRow, startOfCol, endOfRow, endOfCol = position
  if value == 'turn on ':
    change = 1
  elif value == 'toggle ':
    change = 2
  else:
    change = -1
  for i in range(startOfRow, endOfRow+1):
    for j in range(startOfCol, endOfCol+1):
      lightField[i][j] += change
      lightField[i][j] = 0 if lightField[i][j] < 0 else lightField[i][j]

lights2 = generateLightField(1000)

for i in listOfInstructions:
  position = [int(i[1]), int(i[2]), int(i[3]), int(i[4])]
  switchBrigthness(position, i[0], lights2)

sumOfBrightness = countValue(lights2)
print(f'The total brightness of all the lights is about {sumOfBrightness}.')
