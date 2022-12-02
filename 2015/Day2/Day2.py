# Advent of Code Day 2: I Was Told There Would Be No Math

f = open('2015/Day2/Day2.txt', 'r')
raw = f.read().split('\n')
listOfMeasurements = list(map(lambda x: x.split('x'), raw))

totalPaper = 0
totalRibbon = 0

for i in listOfMeasurements:
  val = [int(i[0]), int(i[1]), int(i[2])]

  # Part 1
  side1 = val[0] * val[1]
  side2 = val[1] * val[2]
  side3 = val[0] * val[2]
  smallest = min(side1, side2, side3)
  totalPaper += 2 * (side1 + side2 + side3) + smallest

  # Part 2
  maxVal = max(val[0], val[1], val[2])
  volume = val[0] * val[1] * val[2]
  val.remove(maxVal)
  ribbon = 2 * (val[0] + val[1])
  totalRibbon += ribbon + volume

print(f'The elves need a total of {totalPaper} square feet of wrapping paper for the presents')
print(f'The elves need a total of {totalRibbon} feet of ribbon for the presents')
