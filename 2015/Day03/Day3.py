# Advent of Code Day 3: Perfectly Spherical Houses in a Vacuum

f = open('2015/Day03/Day3.txt', 'r')
data = f.read()

moves = {
  '^': [0, 1],
  'v': [0, -1],
  '>': [1, 0],
  '<': [-1, 0]
}

# Part 1
def startGivingPresents(data, moves):
  santaX = 0
  santaY = 0
  houses = {}
  for i in data:
    santaX += moves[i][0]
    santaY += moves[i][1]
    houses[santaX, santaY] = 1
  return houses

numOfHouses = len(startGivingPresents(data, moves))
print(f'There are {numOfHouses} houses that Santa visited at least once')

# Part 2
def startGivingPresents2(data, moves):
  santaX = 0
  santaY = 0
  roboSantaX = 0
  roboSantaY = 0
  houses = {}
  for i in range(len(data)):
    if i%2 == 1:
      santaX += moves[data[i]][0]
      santaY += moves[data[i]][1]
      houses[santaX, santaY] = 1
    else:
      roboSantaX += moves[data[i]][0]
      roboSantaY += moves[data[i]][1]
      houses[roboSantaX, roboSantaY] = 1
  return houses

numOfHouses2 = len(startGivingPresents2(data, moves))
print(f'There are {numOfHouses2} houses that Santa and Robo-Santa visited at least once')
