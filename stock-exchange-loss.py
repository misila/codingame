import sys, math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
n = int(input())
vs = input()
 
vs = vs.split(' ')
 
 
array = []
 
for x in vs:
    array.append(int(x))
 
more = array[0]
less = array[0]
 
mini = less-more
 
for x in range(len(array)-1):
   
    if array[x]>array[x+1]:
        #if array[x]>more:
        if array[x]>more:
            more = array[x]
        less = array[x]
        if array[x+1]<less:
            less = array[x+1]
   
    if (less-more)<mini:
        mini=less-more
    #print('array[%d]=%d, array[%d]=%d, less=%d, more=%d ' %(x,array[x],x+1, array[x+1],less,more))
 
 
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
 
print(mini)