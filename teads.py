import sys


dico={}
link={}


nb=int(input())
for x in range(nb):
	line=input().split()
	t1,t2=(int(x) for x in line)

	#print('t1=%d, t2=%d' %(t1,t2))
	if t1 in dico:
		dico[t1].append(t2)
	else:
		dico[t1]=[t2]
	if t2 in dico:
		dico[t2].append(t1)
	else:
		dico[t2]=[t1]	


val=0
for k in dico:
  link[k]=len(dico[k])

#print(link)

while len(link)>2:
  leaves = [k for k,v in link.items() if v==1]
  #print('leaves = %s '%str(leaves))
  for item in leaves:    
    myelem =dico[item]
    #print("leaf %d is attached to %s " %(item,str(myelem)))
    for x in myelem:
      if x in link:
        link[x]-=1
    del link[item]

  val+=1

if len(link)==2:
  val+=1
#print('link = %s ' %str(link))
print(val)
  


