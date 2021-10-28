import random
y = random.randrange(10)
z = 0
while z <= 2:
    x = input('Number:')
    if int(x) == y:
        print("!!!!!!!!!YOU WINNNN!!!!!!!!!!!")
        break
    elif int(x) > y:
        if z==2:
            print("GAME OVER"+" random = "+str(y))
            break
        else :print("too big")
    elif int(x) < y:
        if z==2:
            print("GAME OVER"+" random = "+str(y))
            break
        else :print("too small")
    if z==2:
        print("GAME OVER"+" random = "+str(y))
        break
    z += 1
    
        
    
