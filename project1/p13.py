import random
y = random.randrange(10)
x = input('Number:')
if int(x) == y:
    print("Yes!!!!!!!!!!!!!!!!")
elif int(x) > y:
    print("too big")
elif int(x) < y:
    print("too small")
else :print("GAME OVER"+" random = "+str(y))
