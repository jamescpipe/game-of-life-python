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
import time

class cell:
    def __init__(self, state):
        #expects ' ' or '#'
        self.__state = state  
 
    def state(self):
        return self.__state
     
    def set_state(self, state):
        self.__state = state
        return True
        
    def next_state(self):
        return self.__next_state
    
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
                row_cell_list.append(cell(" "))
            self.__grid.append(row_cell_list)
    
    def randomize(self):
        for y in range(0, self.__size):
            for x in range(0, self.__size):
                if random.random() > 0.5:
                    random_state = "#"
                else:
                    random_state = " "
                self.cell(y,x).set_state(random_state)
        return True
    
    def size(self): return self.__size
    
    def print_grid(self): 
        for y in range(0, self.__size):
            row_cell_states = []
            for x in range(0, self.__size):
                row_cell_states.append(self.__grid[y][x].state())
            print(row_cell_states)
    
    def cell(self, y, x): 
        # grid overflows into itself i.e. cell(-1,-1) == cell(n,n)
        size = self.size()
        y = y % size
        x = x % size
        return self.__grid[y][x]
    
    def __cell_occupied_neighbors(self, y, x): 
        currently_alive = (self.cell(y, x).state() == "#")

        # Count occupied neighbors (including own state for simplicity)
        occupied_neighbors = 0
        
        for y_bar in [y-1, y, y+1]:
            for x_bar in [x-1, x, x+1]:
                if self.cell(y_bar, x_bar).state() == "#":
                    occupied_neighbors += 1
                
        if currently_alive:
            occupied_neighbors += -1
            
        return currently_alive, occupied_neighbors
            
    
    def determine_survival(self, y, x):
        
        currently_alive, occupied_neighbors = self.__cell_occupied_neighbors(y, x)
        
        if currently_alive:
            
            if occupied_neighbors in range (0,2) or occupied_neighbors in range (4,9):
                # Death due to loneliness (0 or 1) or overcrowding (4 -> 8)
                return " "
            else: 
                # Survival to the next generation
                return "#"
            
        else:
            if occupied_neighbors == 3:
                # Birth - cell will become occupied next frame
                return "#"
            else:
                return " "
                
    def next_frame(self):
        self.__calc_next_frame()
        for y in range(0, self.__size):
            for x in range(0, self.__size):
                self.cell(y,x).increment_state()
        return True
        
    def __calc_next_frame(self):
        for y in range(0, self.__size):
            for x in range(0, self.__size):
                self.cell(y,x).set_next_state(self.determine_survival(y,x))
        return True
            
    

def test_magic_world_becomes_saturated(myworld):

    test, output, expected = [], [], []
    
    test.append([' ', ' ', '#'])
    test.append([' ', '#', ' '])
    test.append([' ', ' ', '#'])
    
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    
    expected.append(['#', '#', '#'])
    expected.append(['#', '#', '#'])
    expected.append(['#', '#', '#'])

    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            myworld.cell(y,x).set_state(test[y][x])

    myworld.next_frame()
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            output[y][x] = myworld.cell(y,x).state()    

    if output == expected:
        print('Magic world becomes saturated - PASSED')
    else:
        print('Magic world becomes saturated - FAILED')
        print('Test_grid returned as:')
        print (output)
        print('Expected:')
        print (expected)

def test_saturated_world_dies(myworld):

    test, output, expected = [], [], []

    test.append(['#', '#', '#'])
    test.append(['#', '#', '#'])
    test.append(['#', '#', '#'])
    
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    
    expected.append([' ', ' ', ' '])
    expected.append([' ', ' ', ' '])
    expected.append([' ', ' ', ' '])
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            myworld.cell(y,x).set_state(test[y][x])

    myworld.next_frame()
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            output[y][x] = myworld.cell(y,x).state()  
    
    if output == expected:
        print('Saturated world dies - PASSED')
    else:
        print('Saturated world dies - FAILED')
        print('output returned as:')
        print (output)
        print('Expected:')
        print (expected)
    
def test_dead_world_stays_dead(myworld):

    test, output, expected = [], [], []

    test.append([' ', ' ', ' '])
    test.append([' ', ' ', ' '])
    test.append([' ', ' ', ' '])
    
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    
    expected.append([' ', ' ', ' '])
    expected.append([' ', ' ', ' '])
    expected.append([' ', ' ', ' '])
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            myworld.cell(y,x).set_state(test[y][x])

    myworld.next_frame()
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            output[y][x] = myworld.cell(y,x).state()  
    
    if output == expected:
        print('Dead world stays dead - PASSED')
    else:
        print('Dead world stays dead - FAILED')
        print('output returned as:')
        print (output)
        print('Expected:')
        print (expected)    

def test_two_edges_will_die(myworld):

    test, output, expected = [], [], []

    test.append(['#', ' ', ' '])
    test.append(['#', ' ', ' '])
    test.append(['#', '#', '#'])
    
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    
    expected.append([' ', ' ', ' '])
    expected.append([' ', ' ', ' '])
    expected.append([' ', ' ', ' '])
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            myworld.cell(y,x).set_state(test[y][x])

    myworld.next_frame()
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            output[y][x] = myworld.cell(y,x).state()  
    
    if output == expected:
        print('Two edges will be dead - PASSED')
    else:
        print('Two edges will be dead - FAILED')
        print('output returned as:')
        print (output)
        print('Expected:')
        print (expected)  

def test_corners_will_stick(myworld):

    test, output, expected = [], [], []

    test.append(['#', ' ', '#'])
    test.append([' ', ' ', ' '])
    test.append(['#', ' ', '#'])
    
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    
    expected.append(['#', ' ', '#'])
    expected.append([' ', ' ', ' '])
    expected.append(['#', ' ', '#'])
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            myworld.cell(y,x).set_state(test[y][x])

    myworld.next_frame()
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            output[y][x] = myworld.cell(y,x).state()  
    
    if output == expected:
        print('Test corners will stick - PASSED')
    else:
        print('Test corners will stick - FAILED')
        print('output returned as:')
        print (output)
        print('Expected:')
        print (expected)  

def test_down_arrow_saturates(myworld):

    test, output, expected = [], [], []

    test.append(['#', ' ', '#'])
    test.append([' ', '#', ' '])
    test.append([' ', ' ', ' '])
    
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    output.append(['?', '?', '?'])
    
    expected.append(['#', '#', '#'])
    expected.append(['#', '#', '#'])
    expected.append(['#', '#', '#'])
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            myworld.cell(y,x).set_state(test[y][x])

    myworld.next_frame()
    
    for y in range(0,len(test)):
        for x in range(0,len(test[y])):
            output[y][x] = myworld.cell(y,x).state()  
    
    if output == expected:
        print('Test down arrow will saturate - PASSED')
    else:
        print('Test arrow will saturate - FAILED')
        print('output returned as:')
        print (output)
        print('Expected:')
        print (expected) 


def run_random_simulation():
    my_world = world(40)
    my_world.print_grid()
    print("----created-----")
    my_world.randomize()
    my_world.print_grid()
    print("---randomized---")
    
    x = ""

    for i in range(0,100):
        my_world.next_frame()
        my_world.print_grid()
        print("--------------")
        time.sleep(0.1)
        #x = input("Press Enter to continue, x to end")
        
def run_glider():
    myworld = world(8)
    myworld.print_grid()
    print("----created-----")

    glider = [['#', ' ', ' '],
              [' ', '#', '#'],
              ['#', '#', ' ']]

    for y in range(0,len(glider)):
        for x in range(0,len(glider[y])):
            myworld.cell(y,x).set_state(glider[y][x])

    myworld.print_grid()
    print("---glider created---")
    
    x = ""

    for i in range(0,100):
        myworld.next_frame()
        myworld.print_grid()
        print("--------------")
        time.sleep(0.1)
        #x = input("Press Enter to continue, x to end")

def run_glider_gun():
    myworld = world(70)
    myworld.print_grid()
    print("----created-----")

    glider_gun =\
    [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#',' ',' ',' ',' ',' ',' ','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#'],
     [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#'],
     ['#','#',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
     ['#','#',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#','#',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

    for y in range(0,len(glider_gun)):
        for x in range(0,len(glider_gun[y])):
            myworld.cell(y,x).set_state(glider_gun[y][x])

    myworld.print_grid()
    print("---glider gun created---")
    
    x = ""

    for i in range(0,600):
        myworld.next_frame()
        myworld.print_grid()
        print("--------------")
        time.sleep(0.1)
        #x = input("Press Enter to continue, x to end")


def run_test_suite():

    myworld = world(3)
    
    test_magic_world_becomes_saturated(myworld)
    test_saturated_world_dies(myworld)
    test_dead_world_stays_dead(myworld)
    test_two_edges_will_die(myworld)
    test_corners_will_stick(myworld)
    test_down_arrow_saturates(myworld)
    
if __name__ == "__main__":    
    
    run_test_suite()
    #run_random_simulation()
    #run_glider()
    run_glider_gun()