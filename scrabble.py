import sys
 
def findletter(l, w):
    res=-1
    i=0
    for x in w:
        if x==l:
            res=i
            break
        i+=1   
 
    return res
 
nbletters = int(input())
 
dico = []
 
for x in range(nbletters):
    dico.append(input())
 
characters = input()
 
possible = []
nlist    = []
 
for x in dico:
    if len(x)<= len(characters):
        possible.append(x)
        nlist.append(x)
 
 
 
#print(nlist)
 
 
for x in possible:
    #print('%s : ' %x)
    for y in range(len(x)):
        ind=findletter(x[y], characters)
        if ind==-1:
            if x in nlist:
                nlist.remove(x)
                #print('remove %s from list' %x)
                break
        #else :
          #  print('find %c in %s = %d' %(x[y], characters,ind))
 
print(nlist)
lword = { 'e':1,'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,'u':1,
          'd':2,'g':2,
          'b':3,'c':3,'m':3,'p':3,
          'f':4,'h':4,'v':4,'w':4,'y':4,
          'k':5,
          'j':8,'x':8,
          'q':10,'z':10
        }
 
def countvalue(word):
    value=0
    for x in range(len(word)):
        if word[x] in lword:
            #print("word[x]=%c, value = %d" %(word[x],lword.get(word[x])))
            value += lword.get(word[x])
 
    return value
   
wordMax = ""
valueMax = 0
for x in nlist:
    word = ''
    #print(x)
    charac = characters
    for y in range(len(x)):
       
        ind=findletter(x[y], charac)
        #print('search letter %c dans %s, ind=%d ' %(x[y],charac, ind))
        if ind!=-1:
            l = len(charac)-1
            #print('enlever le caractere %c à l indice %d dans %s, len(characters)-1=%d' %(x[y],ind, characters, l))
            if ind==0:
                sentence = charac[1:len(characters)]
                charac = sentence
            elif ind==len(charac)-1:
                sentence = charac[0:ind]
            else :
                sentence = charac[0:ind]
                #print ("sentence av = %s" %characters[0:ind])
                sentence += charac[ind+1:len(charac)]
                #print ("sentence ap = %s" %characters[ind+1:len(characters)])
 
            #print(sentence)
            charac = sentence
            word+=x[y]
    #print (" word = %s" %word)
    if word==x:   
        #lword.append(word)
        vmax=countvalue(word)
        if vmax>valueMax:
            wordMax=word
            valueMax=vmax
 
print(wordMax)