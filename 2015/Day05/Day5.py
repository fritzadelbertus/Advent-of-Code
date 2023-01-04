# Advent of Code Day 5: Doesn't He Have Intern-Elves For This?

f = open('2015/Day5/Day5.txt', 'r')
listOfStrings = f.read().split('\n')

# Part 1
def requirement1 (target):
  counter = 0
  for i in target:
    if i in 'aiueo':
      counter += 1
  return True if counter >=3 else False

def requirement2(target):
  for i in range(1, len(target)):
    if target[i] == target [i-1]:
      return True
  return False

def requirement3(target):
  for i in ['ab', 'cd', 'pq', 'xy']:
    if i in target:
      return False
  return True

niceStrings1 = 0
for i in listOfStrings:
  if requirement1(i) and requirement2(i) and requirement3(i):
    niceStrings1 += 1

print(f'The number of nice strings are {niceStrings1} according to the three rules')


# Part 2
def requirement4(target:str):
  for i in range(1, len(target)):
    if target.count(target[i-1] + target [i]) > 1:
      return True
  return False

def requirement5(target):
  for i in range(2, len(target)):
    if target[i] == target [i-2]:
      return True
  return False

niceStrings2 = 0
for i in listOfStrings:
  if requirement4(i) and requirement5(i):
    niceStrings2 += 1

print(f'The number of nice strings are {niceStrings2} according to the two new rules')
