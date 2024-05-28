# Learn recurssion by solving the Hanoi Puzzle
# The Hanoi Puzzle is a classic problem that can be solved using recursion
# The problem is as follows:
# There are three poles and a number of disks of different sizes which can slide onto any pole.
# The puzzle starts with the disks in a neat stack in ascending order of size on one pole, the smallest at the top.
# The objective of the puzzle is to move the entire stack to another pole, obeying the following rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the top disk from one of the stacks and placing it on top of another stack.
# 3. No disk may be placed on top of a smaller disk.
# The puzzle can be solved in 2^n - 1 moves where n is the number of disks.

# The puzzle can be solved using recursion as follows:
# 1. Move n - 1 disks from the source pole to the auxiliary pole
# 2. Move the nth disk from the source pole to the destination pole
# 3. Move the n - 1 disks from the auxiliary pole to the destination pole
# The base case for the recursion is when there is only one disk to move.
# In this case, the disk is moved directly from the source pole to the destination pole.

NUMBER_OF_DISKS = 3
number_of_moves = 2 ** NUMBER_OF_DISKS - 1

rods = {
  'A': [],
  'B': [],
  'C': []
}

rods['A'] = list(range(3, 0, -1))

def move(n, source, auxiliary, target):
  pass