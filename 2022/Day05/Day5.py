# Advent of Code Day 5: Supply Stacks

f = open('2022/Day05/Day5.txt', 'r')
data = f.read().split('\n')
listOfInstruction = list(map(lambda x: x.split(' '), data))

class Stack(object):
  def __init__(self, stack:list):
    self.stack = stack

  def addStack(self, value):
    self.stack.extend(value)

  def removeStack(self, num=1):
    removed = self.stack[len(self.stack)-num:]
    self.stack = self.stack[:len(self.stack)-num]
    return removed

  def add(self, value):
    self.stack.append(value)

  def remove(self):
    return self.stack.pop()

  def top(self):
    return self.stack[len(self.stack)-1]

def createStack():
  return {
    '1': Stack(['G', 'D', 'V', 'Z', 'J', 'S', 'B']),
    '2': Stack(['Z', 'S', 'M', 'G', 'V', 'P']),
    '3': Stack(['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F']),
    '4': Stack(['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q']),
    '5': Stack(['C', 'L', 'S', 'N', 'F', 'M', 'D']),
    '6': Stack(['R', 'G', 'C', 'D']),
    '7': Stack(['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q']),
    '8': Stack(['P', 'F', 'V']),
    '9': Stack(['D', 'R', 'S', 'T', 'J'])
  }

# Part 1
crates1 = createStack()
for i in listOfInstruction:
  for j in range(int(i[1])):
    val = crates1[i[3]].remove()
    crates1[i[5]].add(val)
answerList1 = [crates1[i].top() for i in crates1]
answer1 = ''
for i in answerList1:
  answer1 += i
print(f'The crates that ends up on top of each stack after the rearrangements from CrateMover 9000 are {answer1}')

# Part 2
crates2 = createStack()
for i in listOfInstruction:
  val = crates2[i[3]].removeStack(int(i[1]))
  crates2[i[5]].addStack(val)
answerList2 = [crates2[i].top() for i in crates2]
answer2 = ''
for i in answerList2:
  answer2 += i
print(f'The crates that ends up on top of each stack after the rearrangements from CrateMover 9001 are {answer2}')
