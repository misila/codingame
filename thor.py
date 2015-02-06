import sys
import math
 
# Read init information from standard input, if any
 
# Read init information from standard input, if any
line = input()
line=line.split(' ')
lx = int(line[0])
ly = int(line[1])
tx = int(line[2])
ty = int(line[3])
 
#print('ly=%d, lx=%d, ty=%d, tx=%d' %(ly,lx,ty,tx))
while 1:
    # Read information from standard input
    if not(tx >=0 and tx <=40 and ty>=0 and ty <=18):
        break
    e=int(input())
    if e==0:
        break;
    d= math.sqrt((lx-tx)*(lx-tx) + (ly-ty)*(ly-ty))
    if d==0:
        break;
   
    if tx==lx: 
        if ty>ly:
            print("N")
            ty-=1
        elif ty<ly:
            print("S")
            ty+=1
    elif tx<lx:
        if ty==ly:
            print("E")
            tx+=1
        elif ty<ly:
            print("SE")
            ty+=1
            tx+=1
        else:
            print("NE")
            tx+=1
            ty-=1
    else:
        if ty==ly:
            print("W")
            tx-=1
        elif ty<ly:
            print("SW")
            ty+=1
            tx-=1
        else:
            print("NW")
            ty-=1
            tx-=1
       
    e-=1