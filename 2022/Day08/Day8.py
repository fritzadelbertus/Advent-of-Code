# Advent of Code Day 8: Treetop Tree House

class Tree():
  def __init__(self, row, col, height):
    self.row = row
    self.col = col
    self.height = height
    self.top:Tree = None
    self.bottom:Tree = None
    self.left:Tree = None
    self.right:Tree = None

  def connectNeighbors(self, top, bottom, left, right):
    self.top = top
    self.bottom = bottom
    self.left = left
    self.right = right

  def topVisible(self, height):
    return self.top if self.top == None or self.top.height >= height else self.top.topVisible(height)
  
  def bottomVisible(self, height):
    return self.bottom if self.bottom == None or self.bottom.height >= height else self.bottom.bottomVisible(height)
  
  def leftVisible(self, height):
    return self.left if self.left == None or self.left.height >= height else self.left.leftVisible(height)
  
  def rightVisible(self, height):
    return self.right if self.right == None or self.right.height >= height else self.right.rightVisible(height)

  def visible(self, height):
    return self.topVisible(height) == None or self.bottomVisible(height) == None or self.leftVisible(height) == None or self.rightVisible(height) == None

  def getScenicScore(self, height, x, y):
    topTree = self.topVisible(height) 
    bottomTree = self.bottomVisible(height) 
    leftTree = self.leftVisible(height) 
    rightTree = self.rightVisible(height) 
    
    top = self.row if topTree == None else self.row - topTree.row
    bottom = y-1-self.row if bottomTree == None else bottomTree.row - self.row
    left = self.col if leftTree == None else self.col - leftTree.col
    right = x-1-self.col if rightTree == None else rightTree.col - self.col

    return top * right * bottom * left

class Forest():
  def __init__(self):
    self.map = []

  def createMap(self, map):
    for i in range(len(map)):
      row = []
      for j in range(len(map[i])):
        row.append(Tree(int(i), int(j), int(map[i][j])))
      self.map.append(row)

  def connectTrees(self):
    for i in range(len(self.map)):
      for j in range(len(self.map[i])):
        top = None if i == 0 else self.map[i-1][j]
        left = None if j == 0 else self.map[i][j-1]
        bottom = None if i == len(self.map)-1 else self.map[i+1][j]
        right = None if j == len(self.map[i])-1 else self.map[i][j+1]
        self.map[i][j].connectNeighbors(top, bottom, left, right)

  def countVisibility(self):
    visibility = 0

    for row in self.map:
      for tree in row:
        if tree.visible(tree.height):
          visibility += 1

    return visibility

  def locateMaxScenicScore(self):
    max = 0

    x = len(self.map[0])
    y = len(self.map)
    for row in self.map:
      for tree in row:
        score = tree.getScenicScore(tree.height, x, y)
        if score > max:
          max = score

    return max
  

f = open('2022/Day8/Day8.txt', 'r')
data = f.read().split('\n')

forest = Forest()
forest.createMap(data)
forest.connectTrees()

# Part 1
visibleTrees = forest.countVisibility()
print(f'There are {visibleTrees} trees which are visible from outside the grid')
# Part 2
maxSceniceScore = forest.locateMaxScenicScore()
print(f'The highest scenic score for a tree inside the forest is {maxSceniceScore}')