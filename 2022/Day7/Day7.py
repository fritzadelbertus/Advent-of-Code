# Advent of Code Day 7: No Space Left On Device

class File():
  def __init__(self, name, value):
    self.size = value
    self.name = name

class Folder():
  def __init__(self, name, parent):
    self.name = name
    self.parent:Folder = parent
    self.innerFolders = []
    self.files = []
    self.size = 0

  def updateSize(self, size):
    self.size += size
    if self.parent != None:
      self.parent.updateSize(size)
    
  def addFolder(self, folder):
    self.innerFolders.append(folder)

  def addFile(self, file:File):
    self.files.append(file)
    self.updateSize(file.size)
  
  def searchFolder(self, target):
    if target == '..':
      return self.parent
    for folder in self.innerFolders:
      if folder.name == target:
        return folder

root = Folder('/', None)

f = open('2022/Day7/Day7.txt', 'r')
data = f.read().split('\n')

pointer = root

for i in range(len(data)):
  if data[i].startswith('$ cd'):
    targetDir = data[i].split(' ')[-1]
    if targetDir == '/':
      pointer = root
    else:
      pointer = pointer.searchFolder(targetDir)
  elif data[i].startswith('$ ls'):
    i = i + 1
    while i < len(data) and data[i].startswith('$') == False:
      box = data[i].split(' ')
      if data[i].startswith('dir'):
        pointer.addFolder(Folder(box[-1], pointer))
      else:
        pointer.addFile(File(box[-1], int(box[0])))
      i += 1
    i = i-1


# Part 1
folders1 = []

def traverseDir(node=root):
  if node.size <= 100000:
    folders1.append(node.size)
  for folder in node.innerFolders:
    traverseDir(folder)

traverseDir()

sumOfFolderSize = 0
for i in folders1:
  sumOfFolderSize += i
print(f'The sum of the total sizes of directories with size of at most 100000 is {sumOfFolderSize}')

# Part 2
freeSpace = 70000000 - root.size
spaceToFree = 30000000 - freeSpace

folders2 = []

def traverseDir(node=root):
  if node.size >= spaceToFree:
    folders2.append(node.size)
  for folder in node.innerFolders:
    traverseDir(folder)

traverseDir()
smallestDirToDelete = min(folders2)
print(f'The size of the smallest directory that would free up enough space for the update is {smallestDirToDelete}')
