# Advent of Code Day 1: The Tyranny of the Rocket Equation

f = open('2019/Day01/Day1.txt', 'r')
data = f.read().split('\n')

fuels1 = 0
for number in data:
  fuels1 += int(int(number)/3) - 2

print(f'The sum of the fuel requirements for part 1 is {fuels1}')

fuels2 = 0
for number in data:
  fuel = int(int(number)/3) - 2
  while fuel > 0:
    fuels2 += fuel
    fuel = int(int(fuel)/3) - 2
  
print(f'The sum of the fuel requirements for part 2 is {fuels2}')