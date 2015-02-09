
import gol_main
import time


### Simulations ###
def run_random_simulation():
    my_world = gol_main.world(40)
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
def run_glider():
    myworld = gol_main.world(8)
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

def run_glider_gun():
    myworld = gol_main.world(70)
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
        
        
if __name__ == "__main__":    

    run_random_simulation()
    #run_glider()
    #run_glider_gun()