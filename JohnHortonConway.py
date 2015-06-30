import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(input())
L = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


car=R

tmpnl=[car]

for x in range(L-1):
    nl=tmpnl
    tmpnl=[]
    car=nl[0]
    count=1
    length=len(nl)
    for y in range(1,length):
        if nl[y]==car:
            count+=1
        else:
            tmpnl.append(count)
            tmpnl.append(car)
            car=nl[y]
            count=1
    tmpnl.append(count)
    tmpnl.append(nl[length-1])
    count=0

liste=tmpnl[:len(tmpnl)-1]

sentence=''
for elem in liste:
    sentence+=str(elem)
    sentence+=' '
    
sentence+= str(tmpnl[len(tmpnl)-1])

print(sentence)
