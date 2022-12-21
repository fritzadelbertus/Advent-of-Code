# Advent of Code Day 3: Binary Diagnostic

f = open('2021/Day3/Day3.txt', 'r')
listOfBinary = f.read().split('\n')

# Part 1
def solve1(binaries):
  gamma = ''
  epsilon = ''
  for i in range(len(binaries[0])):
    count1=0
    count0=0
    for binary in binaries:
      if binary[i] == '1':
        count1 += 1
      else:
        count0 += 1
    if count1 > count0:
      gamma += '1'
      epsilon += '0'
    else:
      gamma += '0'
      epsilon += '1'
  return (int(gamma, 2))*int(epsilon,2)

answer1 = solve1(listOfBinary)
print(f'The power consumption of the submarine is {answer1}')

# Part 2
def solve2(binaries, target):
  result = binaries
  for i in range(len(binaries[0])):
    count1=0
    count0=0
    for binary in result:
      if binary[i] == '1':
        count1 += 1
      else:
        count0 += 1
    if target == 'Oxygen':
      if count1 >= count0:
        result = list(filter(lambda x: x[i] == '1',result))
      else: 
        result = list(filter(lambda x: x[i] == '0',result))
    elif target == 'Carbon':
      if count0 <= count1:
        result = list(filter(lambda x: x[i] == '0',result))
      else: 
        result = list(filter(lambda x: x[i] == '1',result))
    if len(result) == 1:
        break
  return int(result[0],2)

filterOxy = solve2(listOfBinary, 'Oxygen')
filterCarbo = solve2(listOfBinary, 'Carbon')
answer2 = filterOxy * filterCarbo
print(f'The life support rating of the submarine is {answer2}')