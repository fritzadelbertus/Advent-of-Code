# Advent of Code Day 1: Not Quite Lisp

f = open('2015/Day01/Day1.txt', 'r')
data = f.read()

# Part 1
floor = 0
for i in data:
  if i == '(':
    floor += 1
  else:
    floor -= 1
print(f'The instructions took Santa to the {floor}th floor')

# Part 2
counter = 0
floor = 0
while floor != -1 and counter < len(data):
  if data[counter] == '(':
    floor += 1
  else:
    floor -= 1
  counter += 1
print(f'The {counter}th position caused Santa to enter the basement')
