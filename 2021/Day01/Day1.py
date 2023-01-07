# Advent of Code Day 1: Sonar Sweep

f = open('2021/Day01/Day1.txt', 'r')
raw = f.read().split('\n')
listOfDepth = list(map(lambda x: int(x), raw))

# Part 1
increasein1 = 0
for i in range(1, len(listOfDepth)):
  if listOfDepth[i] > listOfDepth [i-1]:
    increasein1 += 1
print(f'The number of times the depth increase is {increasein1}')

# Part 2
increasein3 = 0
for i in range(3, len(listOfDepth)):
  if listOfDepth[i] > listOfDepth [i-3]:
    increasein3 += 1
print(f'The number of times the sum is larger than the previous sum is {increasein3}')