# Advent of Code Day 4: Camp Cleanup

import re
f = open('2022/Day4/Day4.txt', 'r')
data = f.read().split('\n')
pairs = []
for i in data:
  pairs.append(re.search(r'(\d+)-(\d+),(\d+)-(\d+)', i).groups())

fullyOverlap = 0
partiallyOverlap = 0

# Part 1 Logic
def subset(l1, l2, u1, u2):
  if (l1 <= l2 and u1 >= u2) or (l2 <= l1 and u2 >= u1):
    return 1
  return 0

# Part 2 Logic
def intersect(l1, l2, u1, u2):
  if (l1 >= l2 and l1 <= u2) or (l2 >= l1 and l2 <= u1):
    return 1
  return 0

for pair in pairs:
  lbound1 = int(pair[0])
  ubound1 = int(pair[1])
  lbound2 = int(pair[2])
  ubound2 = int(pair[3])
  fullyOverlap += subset(lbound1, lbound2, ubound1, ubound2)
  partiallyOverlap += intersect(lbound1, lbound2, ubound1, ubound2)

print(f'The number of pairs that fully overlap each other are {fullyOverlap}')
print(f'The number of pairs that fully or partially overlap each other are {partiallyOverlap}')
