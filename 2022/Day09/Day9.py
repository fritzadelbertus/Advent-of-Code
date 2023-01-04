# Advent of Code Day 9: Rope Bridge

class Rope():
  def __init__(self, tail=None, record=None):
    self.val = {'x':0, 'y':0}
    self.tail:Rope = tail
    self.record:list = record

  def isTailConnected(self):
    if self.tail == None:
      return True
    return True if  abs(self.val['x'] - self.tail.val['x']) <= 1 and abs(self.val['y'] - self.tail.val['y']) <= 1 else False
  
  def moveTail(self):
    if abs(self.val['x'] - self.tail.val['x']) == 2:
      if self.val['y'] > self.tail.val['y']:
        self.tail.val['y'] += 1
      elif self.val['y'] < self.tail.val['y']:
        self.tail.val['y'] -= 1
      if self.val['x'] - self.tail.val['x'] == 2:
        self.tail.move('R')
      else:
        self.tail.move('L')
      return
    if abs(self.val['y'] - self.tail.val['y']) == 2:
      if self.val['x'] > self.tail.val['x']:
        self.tail.val['x'] += 1
      elif self.val['x'] < self.tail.val['x']:
        self.tail.val['x'] -= 1
      if self.val['y'] - self.tail.val['y'] == 2:
        self.tail.move('U')
      else:
        self.tail.move('D')
      return
    return
  
  def updateRecord(self):
    if [self.val['x'], self.val['y']] not in self.record:
      self.record.append([self.val['x'], self.val['y']])
    return
  
  def move(self, move):
    if move == 'U':
      self.val['y'] += 1
    elif move == 'D':
      self.val['y'] -= 1
    elif move == 'R':
      self.val['x'] += 1
    elif move == 'L':
      self.val['x'] -= 1
  
    if self.isTailConnected() == False:
      self.moveTail()
    if self.record != None:
      self.updateRecord()
    return


rope9 = Rope(None, [[0,0]])
rope8 = Rope(rope9)
rope7 = Rope(rope8)
rope6 = Rope(rope7)
rope5 = Rope(rope6)
rope4 = Rope(rope5)
rope3 = Rope(rope4)
rope2 = Rope(rope3)
rope1 = Rope(rope2, [[0,0]])
head = Rope(rope1)


f = open('2022/Day9/Day9.txt', 'r')
data = f.read().split('\n')

listOfInstructions = list(map(lambda x: x.split(' '), data))

for eachIns in listOfInstructions:
  move = eachIns[0]
  iteration = int(eachIns[-1])
  for i in range(iteration):
    head.move(move)

part1 = len(rope1.record)
print(f'The number of position the rope tail visit in the first part is {part1}')

part2 = len(rope9.record)
print(f'The number of position the rope tail visit in the second part is {part2}')
