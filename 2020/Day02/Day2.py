# Advent of Code Day 2: Password Philosophy

import re
f = open('2020/Day02/Day2.txt', 'r')

input = f.read().split('\n')

passwords = []
for line in input:
  groups = re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
  passwords.append([int(groups[0]), int(groups[1]), groups[2], groups[3]])

def part1(passwords):
  valid = 0
  for key in passwords:
    counter = 0
    for i in key[-1]:
      if i == key[-2]:
        counter += 1
    if counter >= key[0] and counter <= key[1]:
      valid += 1
  return valid

answer1 = part1(passwords)
print(f'There are {answer1} valid passwords according to the first policy rules')

def part2(passwords):
  valid = 0
  for key in passwords:
    leftPos = key[0] - 1
    rightPos = key[1] - 1
    if key[-1][leftPos] == key[-2] and key[-1][rightPos] != key[-2]:
      valid += 1
    elif key[-1][rightPos] == key[-2] and key[-1][leftPos] != key[-2]:
      valid += 1
  return valid

answer2 = part2(passwords)
print(f'There are {answer2} valid passwords according to the second policy rules')
