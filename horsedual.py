import sys
 
nbhorses = int(input())
 
array = []
for x in range(nbhorses):
    array.append(int(input()))
 
array.sort()
 
#print(array)
 
 
minival = array[1] - array[0]
 
for x in range(2,len(array)):
    #print('%d - %d = %d' %(array[x],array[x-1],array[x]-array[x-1]))
    if (array[x]-array[x-1])<minival:
        minival = array[x]-array[x-1]
 
print(minival)