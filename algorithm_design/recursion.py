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

NUMBER_OF_DISKS = 4
number_of_moves = 2 ** NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def make_allowed_move(rod1, rod2):
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())

    # display our progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)

# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')