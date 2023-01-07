# Advent of Code Day 7: Some Assembly Required

# Useful Resource: https://dev.to/jules_lewis/advent-of-code-2015-day-7-35mp

f = open('2015/Day07/Day7.txt', 'r')
raw = f.read().split('\n')

listOfOperation = list(map(lambda x: x.split(' -> '), raw))

operations = {
  'AND': lambda x,y: x & y,
  'OR': lambda x,y:  x | y,
  'NOT': lambda x: ~ x & 65535,
  'RSHIFT': lambda x,y:  x >>  y,
  'LSHIFT': lambda x,y:  x << y & 65535,
}

wires = {}

for i in listOfOperation:
  wires[i[-1]] = i[0].split()

values = {}

def traverse(wire: str):
  if wire.isnumeric():
    return int(wire)
  
  if wire not in values:
    ops = wires[wire]

    if len(ops) == 1:
      n = traverse(ops[0])

    else:
      op = ops[-2]
      if op == 'NOT':
        n = operations[op](traverse(ops[1]))
      else:
        n = operations[op](traverse(ops[0]), traverse(ops[2]))
    values[wire] = n
  
  return values[wire]

# Part 1
wireA = traverse('a')
print(f'The signal provided in wire a is {wireA}')

# Part 2
wires['b'] = [str(wireA)]
values = {}
newWireA = traverse('a')

print(f'When b received the signal from wire a and reset all the wires. The new signal provided in wire a is {newWireA}')
