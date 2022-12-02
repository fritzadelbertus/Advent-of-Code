# Advent of Code Day 2: Rock Paper Scissors

f = open('2022/Day2/Day2.txt', 'r')
raw = f.read().split('\n')
listOfMatches = list(map(lambda x: x.split(' '), raw))
pairs1 = {
  'X':{
    'A': 4, 'B': 1, 'C': 7,
  },
  'Y':{
    'A': 8, 'B': 5, 'C': 2,
  },
  'Z':{
    'A': 3, 'B': 9, 'C': 6,
  },
}

pairs2 = {
  'X':{
    'A': 3, 'B': 1, 'C': 2,
  },
  'Y':{
    'A': 4, 'B': 5, 'C': 6,
  },
  'Z':{
    'A': 8, 'B': 9, 'C': 7,
  },
}

def findScore(matches, pair):
  score = 0
  for i in matches:
    score += pair[i[1]][i[0]]
  return score

solution1 = findScore(listOfMatches, pairs1)
solution2 = findScore(listOfMatches, pairs2)

print(f'The total score for the first problem is {solution1}')
print(f'The total score for the second problem is {solution2}')