import random
import time
list=[0,1,2,3,4,5,6,7,8,9]
pylist=[]
ans=random.randrange(10,999)
def timeout():
    for i in range(5):
        global ans
        ansss=input("What do you think? :")
        if ansss==ans:
            print("WoW so good")
        else: print("You loss")
        time.sleep(1)
    print("timeout")
def py():
    player=input("How many player :")
    for x in range(1,int(player)):
        pylist.append(x)

def play():
    global ans
    print(random.choice(list),random.choice(list),random.choice(list),random.choice(list))
    print(ans)
    timeout()
    
py()
play()