# Advent of Code Day 4: The Ideal Stocking Stuffer

import hashlib

def findNumber(start, target):
  counter = 0
  result = ''
  # Warning: This Loop is using a Brute Force method!
  while result.startswith(target) == False:
    str2hash = start + str(counter)
    theHash = hashlib.md5(str2hash.encode())
    result = theHash.hexdigest()
    counter += 1
  return counter

key = 'iwrupvqb'
input1 = '00000'
input2 = '000000'
answer1 = findNumber(key, input1)
answer2 = findNumber(key, input2)

print(f'The answer to make MD5 hash that starts with {len(input1)} zeros for the key {key} is {answer1}')
print(f'The answer to make MD5 hash that starts with {len(input2)} zeros for the key {key} is {answer2}')
