# Advent of Code Day 1: Report Repair

f = open('2020/Day01/Day1.txt', 'r')

input = f.read().split('\n')
listOfNumbers = list(map(lambda x: int(x),input))

# Part 1
pairs = {}
part1 = None
for number in listOfNumbers:
  if 2020-number in pairs:
    part1 = number
    break
  else:
    pairs[number] = number
result1 = part1 * (2020-part1)
print(f'The product for the two entries that sum up to 2020 is {result1}')

# Part 2
pairs2 = {}
twoPairs = {}
part2 = None
for number in listOfNumbers:
  if 2020-number in twoPairs:
    part2 = number
    break
  else:
    for num in pairs2:
      twoPairs[num+number] = [num, number]
    pairs2[number] = number
  
answer2 = [twoPairs[2020-part2][0], twoPairs[2020-part2][1], part2]
result2 = answer2[0] * answer2[1] * answer2[2]
print(f'The product for the three entries that sum up to 2020 is {result2}')