
from random import random


pi =[]
pyall=[]
pl1=[]
pl2=[]
pl3=[]
pl4=[]
n=0

pi.append("A"+"♠")
pi.append("A"+"♦")
pi.append("A"+"♥")
pi.append("A"+"♣")

for x in range(2,11):
    pi.append(str(x)+"♠")
    pi.append(str(x)+"♦")
    pi.append(str(x)+"♥")
    pi.append(str(x)+"♣")

pi.append("J"+"♠")
pi.append("J"+"♦")
pi.append("J"+"♥")
pi.append("J"+"♣")

pi.append("Q"+"♠")
pi.append("Q"+"♦")
pi.append("Q"+"♥")
pi.append("Q"+"♣")

pi.append("K"+"♠")
pi.append("K"+"♦")
pi.append("K"+"♥")
pi.append("K"+"♣")

player =input("How many player : ")
for allpy in range(1,int(player)+1):
    pyall.append("Player "+str(allpy))

# def kid():
    

def drew(x):
    move = random(0,25)
    pi.insert(pi.index(move,0,52), pyall[x+1])
    pi.remove(move)
    pl1.append(move)
    print(pyall[x+1],"HAVE Pi NUMBER : ",pl1)



# def player3():

# def player4():


def py():
    global player
    if int(player)<=2:
        def player1():
            global n
            drew(-1)
            n=n+1
            if n <=4 :
                player2()
            else :
                print("เสร็จ")
        def player2():
            global n
            drew(-1)
            n=n+1
            if n <=4 :
                player1()
            else :
                print("เสร็จ")
        player1()  
    # if int(player)<=3:
    #     player3()
    # if int(player)<=4:
    #     player4()
    else : 
        print("MAX 4 Player Try agin")
        player =input("How many player : ")
        for allpy in range(1,int(player)+1):
            pyall.append("Player "+str(allpy))
py()
        



