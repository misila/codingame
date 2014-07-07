import sys
 
cara = input()
chaine=''
 
for x in range(0,len(cara)):
    b=bin(ord(cara[x]))[2:]
    l = len(b)
    while l<7:
        b='0'+ b
        l+=1
    chaine+=b
 
length = len(chaine)
 
index  = 0
car = chaine[0]
 
chaine2=''
count=1
 
while (index <length-1):
   
    c=chaine[index+1]
    if (c!=car):
               
                if (car=='0'):
                    chaine2+='00 '
                elif (car=='1'):
                    chaine2+='0 '
                for x in range(count):
                    chaine2+='0'
                count=1
                chaine2+=' '
                index+=1
                car=chaine[index]
    else:
        count+=1
        index+=1
 
 
if (car=='0'):
    chaine2+='00 '
elif (car=='1'):
    chaine2+='0 '
for x in range(count):
    chaine2+='0'
 
 
print(chaine2)