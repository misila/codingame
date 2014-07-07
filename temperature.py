import sys
 
nb = int(input())
 
if (nb<=0):
    print(0)
else :
   
    #print 'nb = %d ' %nb
   
    read = input();
    values = []
    temp = ''
   
    for i in range(0, len(read)):
        if (read[i] == ' '):
            values.append(temp)
            temp =''
        else:
            temp+= read[i]
   
    values.append(temp)
       
    #print values
   
    minitemp = int(values[0])
 
    for i in range(1, len(values)):
        cmp = abs(int(values[i]))
        mini = abs(minitemp)
        if (cmp == mini):
            if (int(values[i]) > 0):
                minitemp = int(values[i])
        elif (cmp<mini):
            minitemp = int(values[i])
           
 
    print(minitemp)