import sys
 
passage=0
hashoot=False
Aller=True
 
 
while 1:
    # Read information from standard input
    line = input()
   
    array = line.split(' ')
   
    sx=int(array[0])
    sy=int(array[1])
 
    mh=[]
    for x in range(8):
        mh.append(int(input()))
 
    if not(hashoot):
        if Aller:          
            max=0
            index=0
            for i in range(8):
               if mh[i]>max:
                   max = mh[i]
                   index = i
        else:
             max=mh[7]
             index=7
             for i,e in reversed(list(enumerate(mh))):
                 if e>max:
                     max   = e
                     index = i
       
        if mh[sx]>0 and sx==index:
            print("FIRE")
            hashoot=True
        else:
            print("HOLD")
    else:
        print("HOLD")
   
    
    if passage<8:       
        passage+=1
        if passage==8:
            Aller=False
            hashoot=False
    else:
        if passage==0:
            Aller=True
            hashoot=False
        passage-=1