# Advent of Code Day 3: Toboggan Trajectory

import re
f = open('2020/Day3/Day3.txt', 'r')

input = f.read().split('\n')

def countTrees(input, slopex, slopey):
  xPos = 0
  yPos = 0
  trees = 0
  while yPos < len(input):
    if xPos >= len(input[yPos]):
      xPos -= len(input[yPos])
    if input[yPos][xPos] == '#':
      trees += 1
    xPos += slopex
    yPos += slopey
  return trees

trees31 = countTrees(input,3,1)
trees11 = countTrees(input,1,1)
trees51 = countTrees(input,5,1)
trees71 = countTrees(input,7,1)
trees12 = countTrees(input,1,2)

part1 = trees31
print(f'The number of trees the toboggan would encounter in the first part is {part1}')

part2 = trees31 * trees11 * trees51 * trees71 * trees12
print(f'The product of the number of trees the toboggan would encounter in the second part is {part2}')
    