N = int(input())
C = int(input())
som = 0
div = C/3
 
maxbudget = []
 
mini = 9223372036854775807
for i in range(N):
    B = int(input())
    maxbudget.append(B)
    if B<mini:
        mini=B
    som += B
maxbudget.sort()
 
print(maxbudget)
 
print(" som = %d " %som)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
 
if som < C:
    print("IMPOSSIBLE")
n=N
 
for x in maxbudget:
    div= int(C/n)
    if x<div:
        print(x)
        C -=x
    else:
        print(div)
        C -=div
    n -=1