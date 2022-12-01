# Advent of Code Day 1: Calorie Counting

f = open('Day 1/Day1.txt', 'r')
raw = f.read().split('\n\n')
listOfCalories = list(map(lambda x: x.split('\n'), raw))
listOfTotalCalories = []
for i in listOfCalories:
  a = 0
  for j in i:
    a += int(j)
  listOfTotalCalories.append(a)
listOfTotalCalories.sort()
elf1 = listOfTotalCalories[-1]
print(f"The Elf with the most calories are {elf1}")
elf2 = listOfTotalCalories[-2]
elf3 = listOfTotalCalories[-3]
print(f"The Elves which have the most calories are {elf1}, {elf2}, {elf3}")
print(f"The sum of the Three Elves with most calories are { elf1 + elf2 + elf3 }")