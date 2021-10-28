import random
list=[1,2,3,4,5,6,7,8,9,10]
game=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

py1=[]
py2=[]


pyall=[]
py=input("Player :")
round=input("How many round do you want to play :")
r = int(round)
n = 0
def movebyplayer():
    global r
    global n
    if n <= r:
        print('---------------------------------------------------------')
        print("Turn "+pyall[0])
        print('---------------------------------------------------------')
        print(game)
        print('---------------------------------------------------------')
        move = input("What is do you want to go :")
        game.insert(game.index(move,0,26), pyall[0])
        game.remove(move)
        py1.append(random.randrange(1,10))
        print(pyall[0],"HAVE NUMBER : ",py1)
        print('---------------------------------------------------------')
        n=n+1
        movebyplayer2()
    else :
        if sum(py1)>sum(py2):
            print(pyall[0]," YOU WIN !")
            print('---------------------------------------------------------')
            print("You Have ")
def movebyplayer2():
    global r
    global n
    if n <= r:
            print("Turn "+pyall[1])
            print('---------------------------------------------------------')
            print(game)
            print('---------------------------------------------------------')
            move = input("What is do you want to go :")
            game.insert(game.index(move,0,26), pyall[1])
            game.remove(move)
            py2.append(random.randrange(1,10))
            print(pyall[1],"HAVE NUMBER : ",py2)
            print('---------------------------------------------------------')
            
            n=n+1
            movebyplayer()
    else :print(pyall[0],"HAVE NUMBER : ",py1,pyall[1],"HAVE NUMBER : ",py2)

for allpy in range(1,int(py)+1):
    pyall.append("Player "+str(allpy))

print(pyall)
print('---------------------------------------------------------')
movebyplayer()


