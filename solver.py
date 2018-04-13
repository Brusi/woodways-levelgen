# A solver class for woodway levels.

from levels import *

# Directions.
left = "l"
right = "r"
up = "u"
down = "d"

teleports = []

def board_copy(board):
    new_board = []
    for line in board:
        new_line = []
        for c in line:
            new_line.append(c)
        new_board.append(line)
    return new_board

def board_get(board, position):
    if position[0] < 0 or position[0] >= len(board):
        return wall
    if position[1] < 0 or position[1] >= len(board[0]):
        return wall
    return board[position[0]][position[1]]

def board_set(board, position, tile):
    word = list(board[position[0]])
    word[position[1]] = tile
    board[position[0]] = "".join(word)

def move_pos(position, direction):
    if direction == up:
        return position[0] - 1, position[1]
    if direction == down:
        return position[0] + 1, position[1]
    if direction == left:
        return position[0], position[1] - 1
    if direction == right:
        return position[0], position[1] + 1

# Moves one animal to the given direction.
# Returns new position if legal, None otherwise.
def move_animal(board, animal, position, direction):
    new_pos = move_pos(position, direction)
    target = board_get(board, new_pos)
    while target == ice:
        position = new_pos
        new_pos = move_pos(new_pos, direction)
        target = board_get(board, new_pos)
    if new_pos in teleports and new_pos != position:
        return teleports[new_pos]
    if target == wall:
        # Ran into wall, does not move.
        return position
    if animal == yak and (target == dirt or target == water):
        return None
    if animal == fox and target == water:
        return None
    return new_pos

# Moves all animals to the given direction.
# Returns new state if move is legal, None otherwise.
def move_all(state, direction):
    board = state[0]
    animals = state[1]
    new_animals = []
    dirt_brakes = []
    for pair in state[1]:
        animal = pair[0]
        pos = pair[1]
        new_pos = move_animal(board, animal, pos, direction)
        if not new_pos:
            return None
        new_animals.append([animal, new_pos])
        if animal == fox and new_pos != pos and board_get(board, pos) == dirt:
            dirt_brakes.append(pos)
        
        
    # Check that no two animals are in the same position.
    positions = set()
    for pair in new_animals:
        if pair[1] in positions:
            return None
        positions.add(pair[1])

    new_board = board_copy(board)

    for dirt_brake_pos in dirt_brakes:
        board_set(new_board, dirt_brake_pos, water)
         
    return (new_board, new_animals)

# Returns true if this state is a win-state (all animals are on portals).
def win(state):
    board = state[0]
    for i,line in enumerate(board):
        for j,c in enumerate(line):
            if c != portal:
                continue
            portal_filled = False
            for pair in state[1]:
                if (i,j) == pair[1]:
                    portal_filled = True
            if not portal_filled:
                return False
    return True

# Prints the board.
def print_board(board):
    for line in board:
        print line

# Prints the board with animals and teleporters.
def print_state(state):
    board_with_animals = board_copy(state[0])
    for pos in teleports:
        board_set(board_with_animals, pos, telep)
    for animal in state[1]:
        pos = animal[1]
        board_set(board_with_animals, pos, animal[0])
    

    print_board(board_with_animals)

# Prints the solution and the board step by step.
def follow_solution(state, sol):
    for direction in sol:
        state = move_all(state, direction)
        print direction
        print_state(state)

# Finds the best solution (least steps) using BFS algorithm. 
def bfs(state_0):
    queue = [(state_0, [])]
    prev_states = [state_0]
    
    solution = None
    while queue:
        state, steps = queue.pop(0)

        # print steps
        # print_state(state)

        for direction in [up, down, left, right]:
            next_state = move_all(state, direction)
            if next_state and next_state not in prev_states:
                solution = steps + [direction]
                if win(next_state):
                    return solution
                    # continue
                
                prev_states.append(next_state)
                queue.append((next_state, solution))

if __name__ == "__main__":
	# An example call to the solver.
    state_0 = (board_45, animals_45)
	
    # TODO: Pass teleports as an argument to the solver and not as a global variable.
    teleports = teleports_45        
	
    print_state(state_0)
    sol = bfs(state_0)
    if sol is None:
        print "no solution"
    else:
        print "Solution:",sol
        follow_solution(state_0, sol)

                    
