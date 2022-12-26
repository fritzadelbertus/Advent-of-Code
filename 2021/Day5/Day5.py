# Advent of Code Day 5: Hydrothermal Venture

f = open('2021/Day5/Day5.txt', 'r')

input = f.read().split('\n')
listOfClouds = list(map(lambda x: x.split(' -> '),input))

class Clouds():
  def __init__(self):
    self.linearCloudMap = [[0 for j in range(990+1)] for i in range(990+1)]
    self.cloudMap = [[0 for j in range(990+1)] for i in range(990+1)]

  def addDiagonalCloud(self, lower, upper, h, hVal):
    while lower <= upper:
      self.cloudMap[lower][h] += 1
      lower += 1
      h += hVal

  def addCloud(self, x1, x2, y1, y2):
    if x1 == x2:
      if y1 > y2:
        y2,y1 = y1,y2
      for i in range(y1, y2 + 1):
        self.cloudMap[i][x1] += 1
        self.linearCloudMap[i][x1] += 1
    elif y1 == y2:
      if x1 > x2:
        x2,x1 = x1,x2
      for i in range(x1, x2 + 1):
        self.cloudMap[y1][i] += 1
        self.linearCloudMap[y1][i] += 1
    else:
      if y1 > y2 and x1 > x2:
        self.addDiagonalCloud(y2,y1,x2, 1)
      elif y1 > y2 and x1 < x2:
        self.addDiagonalCloud(y2,y1,x2, -1)
      elif y1 < y2 and x1 > x2:
        self.addDiagonalCloud(y1,y2,x1, -1)
      else:
        self.addDiagonalCloud(y1,y2,x1, 1)
  
  def countOverlap(self, target):
    clouds = self.linearCloudMap if target == 'Part 1' else self.cloudMap
    count = 0
    for i in clouds:
      for j in i:
        if j >= 2:
          count += 1
    return count

clouds = Clouds()
for cloud in listOfClouds:
  start = cloud[0].split(',')
  end = cloud[1].split(',')
  clouds.addCloud(int(start[0]),int(end[0]),int(start[1]),int(end[1]))

part1 = clouds.countOverlap('Part 1')
print(f'There are {part1} points in the first part where at least two lines overlap')
part2 = clouds.countOverlap('Part 2')
print(f'There are {part2} points in the second part where at least two lines overlap')
