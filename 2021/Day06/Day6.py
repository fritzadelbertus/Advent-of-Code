# Advent of Code Day 6: Lanternfish

f = open('2021/Day6/Day6.txt', 'r')

input = f.read().split(',')
listOfFish = list(map(lambda x: int(x),input))

def countFish(days):
  global listOfFish
  fishRecord = [0,0,0,0,0,0,0,0,0]
  for fish in listOfFish:
    fishRecord[fish] += 1

  for i in range(days):
    temp = fishRecord[0]
    for j in range(8):
      fishRecord[j] = fishRecord[j+1]
    fishRecord[6] += temp
    fishRecord[8] = temp
  
  return sum(fishRecord)

part1 = countFish(80)
print(f'The number of lanternfish after 80 days will be {part1}')
part2 = countFish(256)
print(f'The number of lanternfish after 256 days will be {part2}')
