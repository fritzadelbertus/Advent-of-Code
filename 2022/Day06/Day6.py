# Advent of Code Day 6: Tuning Trouble

f = open('2022/Day06/Day6.txt', 'r')
data = f.read()

def findMarker(datastream, mark):
  marker = 0
  message = ''
  for i in range(len(datastream)):
    if datastream[i] in message:
      message = message[message.find(datastream[i])+1:]
    message += datastream[i]
    if len(message) == mark:
      marker = i 
      break
  return marker + 1

packerMarker = findMarker(data, 4)
messageMarker = findMarker(data, 14)

print(f'{packerMarker} characters need to be processed before the first start-of-packet marker is detected')
print(f'{messageMarker} characters need to be processed before the first start-of-message marker is detected')