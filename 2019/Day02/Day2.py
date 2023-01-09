# Advent of Code Day 2: 1202 Program Alarm

import copy

f = open('2019/Day02/Day2.txt', 'r')
data = f.read().split(',')

opcodes = list(map(lambda x: int(x), data))

def checkOutput(opCodes, noun, verb):
  codes = copy.deepcopy(opCodes)
  codes[1] = noun
  codes[2] = verb
  for i in range(0, len(codes), 4):
    if codes[i] == 99:
      break
    elif codes[i] == 1:
      firstNum = codes[codes[i+1]]
      secondtNum = codes[codes[i+2]]
      res = firstNum + secondtNum
      codes[codes[i+3]] = res
    elif codes[i] == 2:
      firstNum = codes[codes[i+1]]
      secondtNum = codes[codes[i+2]]
      res = firstNum * secondtNum
      codes[codes[i+3]] = res
  return codes[0]

part1 = checkOutput(opcodes, 12, 2)
print(f'The value for position 0 is {part1}')

part2 = None
target = 19690720
for i in range(0, 99):
  for j in range(0,99):
    if checkOutput(opcodes, i, j) == target:
      part2 = [i,j]
      break
  if part2 != None:
    break

answer2 = 100 * part2[0] + part2[1]
print(f'The answer for the second part is {answer2}')
