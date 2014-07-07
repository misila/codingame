import sys
 
dico=dict()
 
 
N = int(input())
Q = int(input())
 
   
for x in range(N):
    l=input()
    l=l.strip()
    word = l.split(' ')
    ext  = word[0].lower()
    mime = word[1]
    if len(mime) <=256 and len(ext)<=50:
        if not(ext in dico):
            dico[ext]=mime
 
#print(dico)
 
for y in range(Q):
    name=input()
    name=name.strip()
    array=name.split('.')
    #if '' in array:
    #    array.remove('')
    #print(array)
    l=len(array)   
    if l>=2 :
        if len(array[l-1])<=10:
            id=array[l-1].lower()
       
            if '.' in id:
                id.remove('.')
            if id in dico:
                print(dico.get(id))
            else :
                print('UNKNOWN')
        else:
            print('UNKNOWN')
    else:
        print('UNKNOWN')
 