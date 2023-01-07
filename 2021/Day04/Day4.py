# Advent of Code Day 4: Giant Squid

f1 = open('2021/Day04/Day4-boards.txt', 'r')
f2 = open('2021/Day04/Day4-numbers.txt', 'r')
boardsString = f1.read().split('\n\n')
listOfNumbers = f2.read().split(',')

class BingoBoard():
  def __init__(self, boardText):
    self.board = []
    self.track = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    self.bingo = False
    self.createBoard(boardText)

  def createBoard(self, boardText):
    for i in range(0, 5):
      row = []
      for j in range(0,5):
        index = i*15+j*3
        row.append(int(boardText[index: index+2]))
      self.board.append(row)
  
  def checkBingo(self):
    for i in range(0, 5):
      colSum = self.track[0][i] + self.track[1][i] + self.track[2][i] + self.track[3][i] + self.track[4][i]
      rowSum = self.track[i][0] + self.track[i][1] + self.track[i][2] + self.track[i][3] + self.track[i][4]
      if colSum == 5 or rowSum == 5:
        self.bingo = True

  def findValue(self, target):
    for i in range(0, 5):
      for j in range(0,5):
        if self.board[i][j] == target:
          self.track[i][j] = 1
          self.checkBingo()
  
  def evaluateBoard(self):
    result = 0
    for i in range(0, 5):
      for j in range(0,5):
        if self.track[i][j] == 0:
          result += self.board[i][j]
    return result

listOfBoards = []
for boardText in boardsString:
  listOfBoards.append(BingoBoard(boardText))

leaderBoard = []

for number in listOfNumbers:
  i = 0
  j = len(listOfBoards)
  while i < j:
    listOfBoards[i].findValue(int(number))
    if listOfBoards[i].bingo:
      leaderBoard.append({'board': listOfBoards[i], 'winningNumber': int(number)})
      listOfBoards.pop(i)
      i -= 1
      j -= 1
    i += 1

def finalScore(input):
  return input['board'].evaluateBoard() * input['winningNumber']

answer1 = finalScore(leaderBoard[0])
answer2 = finalScore(leaderBoard[-1])

print(f'The final score for the first bingo board that wins is {answer1}')
print(f'The final score for the last bingo board that wins is {answer2}')
