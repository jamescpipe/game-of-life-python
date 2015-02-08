#game of life - James Pipe Feb 2015

"""
From http://www.math.cornell.edu/~lipa/mec/lesson6.html
& http://www.tech.org/~stuart/life/rules.html

The Game of Life (an example of a cellular automaton) is played on an infinite 
two-dimensional rectangular grid of cells. Each cell can be either alive or dead. 
The status of each cell changes each turn of the game (also called a generation) 
depending on the statuses of that cell's 8 neighbors. Neighbors of a cell are cells 
that touch that cell, either horizontal, vertical, or diagonal from that cell.

The initial pattern is the first generation. The second generation evolves from applying 
the rules simultaneously to every cell on the game board, i.e. births and deaths happen 
simultaneously. Afterwards, the rules are iteratively applied to create future 
generations. For each generation of the game, a cell's status in the next generation is 
determined by a set of rules. These simple rules are as follows:

DEATH:    If an occupied cell has 0, 1, 4, 5, 6, 7, or 8 occupied neighbors, 
          the organism dies (0, 1: of loneliness; 4 thru 8: of overcrowding).

SURVIVAL: If an occupied cell has two or three neighbors, 
          the organism survives to the next generation.

BIRTH:    If an unoccupied cell has three occupied neighbors, it becomes occupied.

"""

import random
        
class grid:
    def __init__(self):

        self.__rows = []
        
        self.__rows.append(["_","_","_","A","_","_","_","A","A"])
        self.__rows.append(["_","A","_","_","_","_","_","_","A"])
        self.__rows.append(["_","_","_","A","_","_","_","A","_"])
        self.__rows.append(["_","_","A","_","_","_","A","A","A"])
        self.__rows.append(["_","_","A","A","_","_","A","A","A"])
        self.__rows.append(["A","_","_","_","_","_","A","A","A"])
        self.__rows.append(["_","_","A","_","_","_","_","_","_"])
        self.__rows.append(["_","_","_","_","_","_","_","_","_"])
        self.__rows.append(["_","_","_","_","_","_","_","_","_"])
        self.__rows.append(["_","_","_","A","_","_","_","_","_"])

    def rows(self):
        return self.__rows
    
    def cell(self, y, x):
        return self.__rows[y][x]

class cell:
    def __init__(self):
        
        if random.random() > 0.5:
            self.__state = "A"
        else:
            self.__state = "_"
                
    def state(self):
        return self.__state
    
    def set_next_state(self, next_state):
        self.__next_state = next_state
        return True
        
    def increment_state(self):
        self.__state = self.__next_state
        return True

class world:
    def __init__(self, size):
        
        self.__grid = []
        self.__size = size
        
        for y in range(0, size):
            row_cell_list = []
            for x in range(0, size):
                row_cell_list.append(cell())
            self.__grid.append(row_cell_list)
    
    def size(self): return self.size
    
    def print_grid(self): 
        for y in range(0, self.__size):
            row_cell_states = []
            for x in range(0, self.__size):
                row_cell_states.append(self.__grid[y][x].state())
            print(row_cell_states)
                
            
    
    def cell(self, y, x): return self.__grid[y][x].state()
        
        
W = world(9)
W.print_grid()
            
print('Cell in 0,3 is ' + W.cell(0, 3))
print('Cell in 1,3 is ' + W.cell(1, 3))        
        
        


G = grid()

for y in G.rows():
    print(y)
            
print('This should be A - ' + G.cell(0, 3))
print('This should be _ - ' + G.cell(1, 3))


