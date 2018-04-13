# Level generator for Woodways.
# Generates random level until a solvable one is found.

from levels import *
from solver import *

import random

# Generates a single tile with weighted probabilities.
# This is a good place to fiddle.
def generate_tile():
    x = random.random()
    if x < 0.4:
        return blank
    if x < 0.7:
        return water
    if x < 0.85:
        return ice
    return dirt

# Returns a list of all blank tiles. Good as candidates for animals and portals.
def find_blanks(board):
    blanks = []
    for i, line in enumerate(board):
        for j, tile in enumerate(line):
            if tile == blank:
                blanks.append((i,j))
    return blanks

# Generates a single board, with portals.
def generate_board(size, num):
    board = []
    for i in xrange(size[0]):
        line=""
        for j in xrange(size[1]):
            line = line + generate_tile()
        board.append(line)

    # Generate portals.
    blanks = find_blanks(board)
    for _ in xrange(num):
        if not blanks:
            return None
        pos = random.choice(blanks)
        board_set(board, pos, portal)
        blanks.remove(pos)
    
    return board

def random_animal():
    x = random.random()
    if x < 0.3333333:
        return duck
    if random < 0.6666666:
        return fox
    return yak

# Generates a list of animals, placed on the blank tiles of board.
def generate_animals(board, num):
    animals = []
    blanks = find_blanks(board)
    for _ in xrange(num):
        if not blanks:
            return None
        pos = random.choice(blanks)
        animals.append([random_animal(), pos])
        blanks.remove(pos)
    return animals

# Tries to generate a solvable level. Often fails and returns None.
# Creates a random board, places animals at random, then tries to solve.
# Returns the board and animals and solution if suceeds, otherwise returns None.
# TODO: Add teleports.
def generate_level(size, num):
    board = generate_board(size, num)
    if not board:
        # Not enough space for portals.
        return None
    animals = generate_animals(board, num)
    if not animals:
        # Not enough space for animals.
        return None
        
    state_0 = (board, animals)
    sol = bfs(state_0)
    if not sol:
        # Not solvable.
        return None

    return (board, animals, sol)

# Brute-force generating levels until finds a legal one, and returns it.
# If min_steps is positive, then this function keeps the searching
# until it finds a level with solution with min_steps steps or more.
def level_search(size, num, min_steps=0):
    print "Searching..."
    while True:
        res = generate_level(size, num)
        if res:
            board, animals, sol = res
            if min_steps > 0 and len(sol) < min_steps:
                # Not enough solution steps, keep searching.
                continue
            return res

if __name__ == "__main__":
	size = (5,5)
	num = 2
	min_steps = 10
	board, animals, sol = level_search(size, num, min_steps)

	print_board(board)
	print animals
	print_state((board, animals))

	print sol
    
