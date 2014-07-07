width  = int(input());
height = int(input());
word   = str(input());
 

alphabet=[]
if len(word)==0:
    print(" word is null")
 
alphindex= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 
for w in range(height):
    alphabet.append(str(input()))
 
 
 
for l in range(height):
    line=''
    for w in word.lower():
        i=alphindex.index(w) if w in alphindex else 26
        start= i*width
        end  = start+width
        line+=alphabet[l][start:end]
    print(line)