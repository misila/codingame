import sys, math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
N = int(input())
 
tableau = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
contact = ()
 
def recursiveContact(contact, indice, number, ind):
 
    if len(number)==ind:
        return contact
   
    if not(contact):
        c = (int(number[ind]),)
        ind +=1
        return recursiveContact(c,indice+1, number, ind)
   
    if indice>=len(contact):
        ni = int(number[ind])
        contact += (ni,)
        ind +=1
        return recursiveContact(contact, indice+1, number, ind)
   
    if type(contact) is list:
       
        c = int(number[ind])
        newn = number[ind:len(number)]
        nl=recursiveContact(contact[c], 0, newn,0)
        print(nl)
        return nl
   
    if type(contact) is tuple:
       
        for i in range(0, len(contact)):
            c=contact[i]
           
            if (type(c) is int):
               
                ci = int(number[ind])
                if c==ci:
                    if ind==i:
                        if ind==(len(number)-1):
                            return contact
                        else:
                            ind+=1
                    else:
                        ind+=1
                        if ind==len(number):
                            return contact
                elif c!=ci:
 
                    newContact=()
                   
                    for x in range(0,i):
                        if type(contact[x]) is int:
                           
                            if contact[x]!=-1:
                                newContact += (contact[x],)
                            else:
                                newContact += (contact[x],)
                               
                    head_contact = ()
                    head_contact+=recursiveContact(head_contact, indice, number, ind)
                   
                    tail_contact = ()
                    index_tail = contact[i]
                   
                    for x in range(i,len(contact)):
                        if type(contact[x]) is int:
                           
                            if contact[x]!=-1:
                                tail_contact += (contact[x],)
                        else:
                            tail_contact += (contact[x],)
                   
            
                    nl = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
                    nl[index_tail]=tail_contact
                    index_head = int(number[ind])
                   nl[index_head]=head_contact
                    newContact+=(nl,)
                    return newContact
                indice+=1
 
           
            elif type(c) is list:
                ci = int(number[ind])
                if c[ci]==-1:
                    nnt=()
                    nnt=recursiveContact((),0,number,ind)
                    c[ci]=nnt
                    return contact
                else:
                    ci = int(number[ind])
                    rn = recursiveContact(c[ci], 0, number, ind)
                    c[ci]=rn
                    return contact
               
        while ind<len(number):
            contact+= (int(number[ind]),)
            ind +=1
       
        return contact
 
 
 
def countNumber(elem):
 
    if type(elem) is tuple:
        som=0
        for x in elem:
            som+=countNumber(x)
       
        return som
   
    elif type(elem) is int:
        if elem==-1:
            return 0
        else:
            return 1
    elif type(elem) is list:
        som=0
        for x in elem:
            som+= countNumber(x)
 
        return som
   
    
        
for i in range(N):
   
    n=input()
    #n=f.readline().strip('\n')
    #print("===> %s " %n)
   if len(n)==0:
        continue
    index=int(n[0])
    if tableau[index]==-1:
        tableau[index]=recursiveContact((), 0, n, 0)
    else:
        tableau[index]=recursiveContact(tableau[index], 0, n, 0)
    #print(tableau[index])
 
 
som=0
for x in tableau:
    #print(x)
    som+=countNumber(x)
    #print('==> som=%d ' %som)
 
print(som)
 
