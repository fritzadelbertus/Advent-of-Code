# Advent of Code Day 4: Passport Processing
import re

f = open('2020/Day04/Day4.txt', 'r')
data = f.read().split('\n\n')

passports = []
for passportData in data:
  passport = {}
  passLine = passportData.split('\n')
  for line in passLine:
    items = line.split(' ')
    for item in items:
      keyValue = item.split(':')
      passport[keyValue[0]] = keyValue[1]
  passports.append(passport)

def checkValid(passport):
  validecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  valid = True
  if (int(passport['byr']) in range(1920,2003)) == False:
    valid = False
  if (int(passport['iyr']) in range(2010,2021)) == False:
    valid = False
  if (int(passport['eyr']) in range(2020,2031)) == False:
    valid = False
  if re.match(r'^#[A-Fa-f0-9]{6}', passport['hcl']) == None:
    valid = False
  if passport['ecl'] not in validecl:
    valid = False
  if passport['pid'].isnumeric() == False or len(passport['pid']) != 9:
    valid = False
  if passport['hgt'].endswith('cm') and (int(passport['hgt'].split('cm')[0]) in range(150,194)) == False:
    valid = False
  elif passport['hgt'].endswith('in') and (int(passport['hgt'].split('in')[0]) in range(59,77)) == False:
    valid = False
  elif passport['hgt'].endswith('in') == False and passport['hgt'].endswith('cm') == False:
    valid = False
  return valid

part1 = 0
part2 = 0

for passport in passports:
  if len(passport) == 8:
    part1 += 1
    if checkValid(passport):
      part2 += 1
  elif len(passport) >= 7:
    noCid = 'cid' not in passport
    if noCid:
      part1 += 1
      if checkValid(passport):
        part2 += 1

print(f'The number of valid passports in the first part is {part1}')
print(f'The number of valid passports in the second part is {part2}')
