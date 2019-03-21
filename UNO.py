#uno
import random

def fill(l):
    colour='R'
    for i in range(10):
        l.append([colour,str(i)])
    colour='B'
    for i in range(10):
        l.append([colour,str(i)])
    colour='Y'
    for i in range(10):
        l.append([colour,str(i)])
    colour='G'
    for i in range(10):
        l.append([colour,str(i)])
    random.shuffle(l)
    return l

def start(l):
    for i in range(7):
        r=random.choice(deck)
        l.append(r)
        deck.remove(r)
    return l

def display():
    print("My Deck:")
    for i in range(len(me)):
        print(i,end='\t')
    print()
    for c in me:
        print(''.join(c),end='\t')
    print('\n')

def play(player,card):
    chosen=0
    for c in player:
        if c[0]==card[0] or c[1]==card[1]:
            card=c
            print(turn,''.join(card),end='')
            player.remove(card)
            used.append(card)
            if len(player)==1:
                print(", UNO!")
            print()
            return card
    r=deck[0]
    player.append(r)
    deck.remove(r)
    print(turn,"T, Card: ",''.join(card))
    return card

def choose_colour(player):
    r=0;b=0;y=0;g=0
    for i in player:
        if i[0]=='R':
            r+=1
        elif i[0]=='B':
            b+=1
        if i[0]=='Y':
            y+=1
        if i[0]=='G':
            g+=1
    choice=max(r,b,y,g)
        
#Setup    
deck=[]
fill(deck)
used=[]
players=['Me: ','P1: ','P2: ','P3: ']
me=[]
start(me)
player1=[]
start(player1)
player2=[]
start(player2)
player3=[]
start(player3)
card=random.choice(deck)
deck.remove(card)
print('Start: ',''.join(card))
t_pos=0
turn=players[t_pos]

#Gameplay
while len(me)!=0 and len(player1)!=0 and len(player2)!=0 and len(player3)!=0:
    if turn=='Me: ':
        display()
        #Check for valid input
        valid=0
        while valid==0:
            p=input("Enter your choice: ")
            if p=='T' or me[int(p)][0]==card[0] or me[int(p)][1]==card[1]:
                valid=1
            else:
                print("Invalid Choice")
        if p=='T':
            r=deck[0]
            me.append(r)
            deck.remove(r)
            print(turn,"T")
        else:
            p=int(p)
            card=me[p]
            print(turn,''.join(card),end='')
            me.remove(card)
            used.append(card)
            if len(me)==1:
                print(", UNO!")
            print()
    elif turn=='P1: ':
      card=play(player1,card)
    elif turn=='P2: ':
      card=play(player2,card)
    elif turn=='P3: ':
        card=play(player3,card)
    #Next Player
    if t_pos==len(players)-1:
        t_pos=0
    else:
        t_pos+=1
    turn=players[t_pos]
    if len(deck)==0:
        random.shuffle(used)
        deck+=used
        used=[]

#Winner
if len(me)==0:
    print("You Win!")
elif len(player1)==0:
    print("Player 1 wins!")
elif len(player2)==0:
    print("Player 2 wins!")
elif len(player3)==0:
    print("Player 3 wins!")


        






        
