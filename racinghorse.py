import sys
import math
 
list = []
 
horses = int(input())
for i in range(horses):
    list.append(int(input()))
   
list.sort()
 
mini=1000000
 
for x in range(len(list)-1):
    m=math.fabs(list[x+1] - list[x])
    if m<mini:
        mini=m
       
        
print(int(mini))