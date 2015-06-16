## Solve APU InitPhase in python 3.0  (MEDIUM)

import sys, math

# Don't let the machines win. You are humanity's last hope...

width = int(input()) # the number of cells on the X axis
height = int(input()) # the number of cells on the Y axis
#print("width = "+str(width)+", height="+str(height))
mat = []
grid = []


for i in range(height):
    line = input() # width characters, each either 0 or .
    #print('line=%s' %line)
    matb=[]
    for j in range(width):
        matb.append(line[j])
        if line[j]=='0':
            grid.append((i,j))
    mat.append(matb)

for elem in grid:
    droit=False
    y=tmpy=elem[0]
    x=tmpx=elem[1]
    resd = "-1 -1"
    while not(droit):
        tmpx+=1
        if tmpx>=width:
            droit=True
        else:
            if mat[y][tmpx]=='0':
                droit=True
                resd="%d %d" %(tmpx,y)
        
    bas=False
    resb = "-1 -1"
    x=elem[1]
    while not(bas):
        tmpy+=1
        if tmpy>=height:
            bas=True
        else:
            if mat[tmpy][x]=='0':
                bas=True
                resb="%d %d" %(x,tmpy)
        
    print("%d %d %s %s" %(x,y,resd,resb))
