import sys, math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
# W: width of the building.
# H: height of the building.
W, H = [int(i) for i in input().split()]
N = int(input()) # maximum number of turns before game over.
X0, Y0 = [int(i) for i in input().split()]
 
x = X0
y = Y0
#print(" H = %d, W = %d " %(H,W))
 
xmin = 0
ymin = 0
 
# game loop
while 1:
    BOMB_DIR = input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
 
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
  
    if BOMB_DIR == "UR":
        xmin=x
        H=y
        y=(ymin+H)/2
        x=(xmin+W)/2
        #print("xmin=%d, ymin=%d, y=%d, x=%d" %(xmin,ymin,y,x))
    if BOMB_DIR == "U":
        H=y
        y=(ymin+H)/2
    if BOMB_DIR == "R":
        x=(x+W)/2
    if BOMB_DIR == "DR":
        ymin=y
        xmin=x
        y=(ymin+H)/2
        x=(x+W)/2
    if BOMB_DIR == "D":
        ymin=y
        y=(ymin+H)/2
    if BOMB_DIR == "DL":
        W=x
        ymin=y
        x=(xmin+W)/2
        y=(ymin+H)/2
        #print(" W=%d, H=%d, x=%d,y=%d, xmin=%d, ymin=%d" %(W,H,x,y,xmin,ymin))
       
    if BOMB_DIR == "L":
        W=x
        x=(xmin+W)/2
    if BOMB_DIR == "UL":
        H=y
        W=x
        x=(xmin+W)/2
        y=(ymin+H)/2
    print ("%d %d " %(x,y))