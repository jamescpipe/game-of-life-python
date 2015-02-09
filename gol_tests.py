
import gol_main

### Game of life Tests - looped infinite board ###
def run_test_suite():

    myworld = gol_main.world(3)
    
    test_magic_world_becomes_saturated(myworld)
    test_saturated_world_dies(myworld)
    test_dead_world_stays_dead(myworld)
    test_two_edges_will_die(myworld)
    test_corners_will_stick(myworld)
    test_down_arrow_saturates(myworld)

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
        
if __name__ == "__main__":    
    
    run_test_suite()