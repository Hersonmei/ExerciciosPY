#Conway's Game of Life

import random, time, copy
WIDTH = 60
HEIGHT = 20

#Creat a list of list for the cells
next_cells = []
for x in range(WIDTH):
    column = [] #creat a new column
    for y in range(HEIGHT):
        if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
            column.append('#') #add a living cell
        else:
            column.append(' ') #add a dead cell
    next_cells.append(column) #next_cells is a list of column lists.

while True: #Main program loop.
    print('\n\n\n\n\n') #Separate each step with newlines.
    currentCells = copy.deepcopy(next_cells)

    #Print currenCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.

    #Calculate the next steps cells based on current steps cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighboring cordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rigthCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rigthCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rigthCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rigthCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            
            # Set cell based on Conwa'ys Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors ==3):
                # Living cells with 2 or 3 neighbors stay alive:
                next_cells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                next_cells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                next_cells[x][y] = ' '
    time.sleep(1) #add a 1-second pause to reduce flickring