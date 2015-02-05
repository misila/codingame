import sys, math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbTotalClones: number of generated clones
# nbAdditionalElevators: ignore (always zero)
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in input().split()]
#print("nbRounds=%d, width=%d, nbFloors=%d" %(nbRounds,width,nbFloors))
 
enough= width*nbFloors < nbRounds
 
elevPos   = []
for i in range(nbElevators):
    elevPos.append(0)
   
for i in range(nbElevators):
    # elevatorFloor: floor on which this elevator is found
    # elevatorPos: position of the elevator on its floor
    elevatorFloor, elevatorPos = [int(i) for i in input().split()]
    #elevFloor.append(elevatorFloor)
    elevPos[elevatorFloor]=elevatorPos
 
    #print("elevPos.insert(%d,%d)" %(elevatorFloor,elevatorPos))
 
#print(elevPos)
 
#print("nbFloor=%d, width=%d, exitFloor=%d, exitPos=%d, nbTotalClones=%d, nbElevators=%d" %(nbFloors,width, nbRounds, exitFloor,exitPos, nbElevators))   
#print(elevPos)
 
# game loop
while 1:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    cloneFloor, clonePos, direction = input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)
   
    #print("cloneFloor=%d, clonePos=%d, direction=%s" %(cloneFloor,clonePos,direction))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if cloneFloor==-1 and clonePos==-1 and direction=='NONE':
        print("WAIT") # action: WAIT or BLOCK
   
    if not(enough):
        if cloneFloor==nbFloors-1:
            if direction=="RIGHT":
                if exitPos<clonePos:
                    print("BLOCK")
                    continue
            elif direction=="LEFT":
                if exitPos>clonePos:
                    print("BLOCK")
                    continue
        else:
            if direction=="RIGHT":
                if elevPos[cloneFloor] < clonePos:
                    print("BLOCK")
                    continue
            elif direction=="LEFT":
                if elevPos[cloneFloor] > clonePos:
                    print("BLOCK")
                    continue
           
    if (clonePos == (width-1) or clonePos==0):
        print("BLOCK")
        continue
    else:
        print("WAIT")