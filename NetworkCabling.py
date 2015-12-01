import math,sys
from collections import OrderedDict

N = int(input())

AbsX = []
OrdY = []


for i in range(N):
    X, Y = [int(i) for i in input().split()]
    AbsX.append(X)
    OrdY.append(Y)

def WestPoint():
    mini=AbsX[0]
    ind=0
    for i in range(N):
        if AbsX[i]<mini:
            mini=AbsX[i]
            ind=i

    return ind

def EastPoint():
    maxi=AbsX[0]
    ind=0
    for i in range(N):
        if AbsX[i]>maxi:
            maxi=AbsX[i]
            ind=i

    return ind

west = WestPoint()
east = EastPoint()

# compute distance for the main cable  between the most westerly building and the most easterly building
distEastWest = int(math.fabs(AbsX[east]-AbsX[west]))
#print(" distEastWest = %d " %distEastWest)

# find the Y where should  be placed the main cable , with mediane computation
sortOrdY = sorted(OrdY)
indM = int(len(sortOrdY)/2)
mediane=sortOrdY[indM]
#print("liste trie OrdY = %s, indM=%d" %(str(sortOrdY),indM))
#print(" startWest = %d, endEast = %d, middle=%d " %(start, end, mediane))


dist=distEastWest
    
# add the distance of vertical cable which connect the building to the main cable
for i in range(len(OrdY)):
  if mediane<=OrdY[i]:
    dist += int(math.fabs((OrdY[i]-mediane)))
  else:
    dist += int(math.fabs((mediane-OrdY[i])))

print(dist)

