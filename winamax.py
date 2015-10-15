import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player1=[]
player2=[]
dicoCard = { '2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,
             '1':9, 'J':10, 'Q':11, 'K':12,'A':13   }
 
 
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    player1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    player2.append(cardp_2)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

war1=[]
war2=[]

count=0


while player1 and player2:
    
    #print('player1=%s' %str(player1))
    #print('player2=%s' %str(player2))

    card1=player1.pop(0)
    card2=player2.pop(0)
    #print('card1=%s, card2=%s ' %(card1,card2))
    c1=card1[0]
    c2=card2[0]
    #print('c1=%s, c2=%s ' %(c1,c2))
    if dicoCard[c1]>dicoCard[c2]:
        war1.append(card1)
        war2.append(card2)
        player1.extend(war1)
        player1.extend(war2)
        war1=[]
        war2=[]
        count+=1
    elif dicoCard[c1]<dicoCard[c2]:
        war1.append(card1)
        war2.append(card2)
        player2.extend(war1)
        player2.extend(war2)
        war1=[]
        war2=[]
        count+=1
    else: # card1==card2 , war
        war1.append(card1)
        war2.append(card2)
        
        for x in range(3):
            if player1 and player2:
                card1=player1.pop(0)
                card2=player2.pop(0)
                war1.append(card1)
                war2.append(card2)
            else:
                player1=[]
                player2=[]
                break


if len(player1)==0:
    if len(player2)==0:
        print('PAT')
    else:
        print('2 %d' %count)
else:
    if len(player2)==0:
        print('1 %d' %count)
