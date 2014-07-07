import sys
import math
 
class Defibrillateur:
 
    #name
    #address
    #phonenumber
    #longitude
    #latitude
 
    def __init__(self,id,n,a,pn,lo,la):
        self.ident      = id
        self.name       = n
        self.address    = a
        self.phonenumber= pn
        self.longitude  = lo
        self.latitude   = la
 
    def display(self):
        print ('ident=%d,name=%s, address=%s,phonenumber=%s,longitude=%f,latitude=%f' %(self.ident,self.name,self.address,self.phonenumber,self.longitude,self.latitude))
 
def readline():
    l=input()
    array=l.split(';')
    id = int(array[0])
    lo = array[4].replace(",",".")
    lo = float(lo)*math.pi/180
    la = array[5].replace(",",".")
    la = float(la)*math.pi/180
    d = Defibrillateur(id,array[1], array[2], array[3], lo, la)
    if (d.ident in data):
        data[i.ident]=d
    #d.display()
    return d
 
def distance(fibri, longU, latU):
    x = (fibri.longitude - longU)* math.cos((fibri.latitude+latU)/2)
    y = fibri.latitude  - latU
    d = math.sqrt(x*x + y*y)*6371
    return d
   
 
data = dict()
 
longU = input()
latiU  = input()
nbdef     = int(input())
 
longU = longU.replace(",",".")
longU = float(longU)*math.pi/180
 
latiU = latiU.replace(",",".")
latiU = float(latiU)*math.pi/180
 
distmini=1000000.0
ident = -1
 
for x in range(nbdef):
    d=readline()
    data[d.ident]=d
    dist = distance(d, longU, latiU)
    #print('%d, %f,distmini=%f' %(d.ident,dist,distmini))
    if dist < distmini:
        distmini=dist
        ident = d.ident
       
 
 
if ident!=-1:   
    print(data[ident].name)