# Advent of Code Day 10: Cathode-Ray Tube

f = open('2022/Day10/Day10.txt', 'r')
data = f.read().split('\n')

cycle = 0
index = 0
addValue = None
value = 1

# For Part 1
signals = []

# For Part 2
draw = ''
message = []

while cycle < 240 and index < len(data):
  cycle += 1
  instruction = data[index]

  # Part 1 Logic
  if cycle in [20,60,100,140,180,220]:
    signals.append(value*cycle)

  # Part 2 Logic
  if len(draw) in [value-1, value, value+1]:
    draw += '#'
  else:
    draw += '.'
  if cycle%40 == 0:
    message.append(draw)
    draw = ''

  # Device Logic
  if instruction == 'noop':
    index += 1
  elif addValue == None:
    addValue = instruction.split(' ')[-1]
  else:
    value += int(addValue)
    addValue = None
    index += 1

part1 = sum(signals)
print(f'The sum of the six signal strengths is {part1}')

print(f'The 8 letter message from the signal:')
for line in message:
  print(line)
