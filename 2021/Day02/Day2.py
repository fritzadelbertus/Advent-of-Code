# Advent of Code Day 2: Dive!

f = open('2021/Day2/Day2.txt', 'r')
raw = f.read().split('\n')
listOfMoves = list(map(lambda x: x.split(' '), raw))

# Part 1
def solve1(moves):
  horiz = 0
  depth = 0
  for move in moves:
    if move[0] == 'forward':
      horiz += int(move[-1])
    elif move[0] == 'down':
      depth += int(move[-1])
    else:
      depth -= int(move[-1])
  return horiz * depth

# Part 2
def solve2(moves):
  horiz = 0
  aim = 0
  depth = 0
  for move in moves:
    if move[0] == 'forward':
      horiz += int(move[-1])
      depth += aim * int(move[-1])
    elif move[0] == 'down':
      aim += int(move[-1])
    else:
      aim -= int(move[-1])
  return horiz * depth

answer1 = solve1(listOfMoves)
answer2 = solve2(listOfMoves)
print(f'The answer for the first part is {answer1}')
print(f'The answer for the second part is {answer2}')