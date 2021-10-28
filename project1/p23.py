mew=[52,2,45,32,58,7,56,4,5,6]
save=[1]
def fac(x,y):
    if x<y:
        factoo(x,y)
    else: print(mew)
def factoo(x,y):
    if x<(y-1):
        if mew[x]<mew[x+1]:
            fac(x+1,y)
        elif mew[x]>mew[x+1]:
            save[0]=mew[x]
            mew[x]=mew[x+1]
            mew[x+1]=save[0]
            print(mew)
            fac(x+1,y)
    elif mew[0]>mew[1] :
        fac(0,y)
    for x in range(0, y):
        if mew[y-1]==max(mew):
            break
        elif mew[x]<mew[x+1]:
            continue
        elif mew[x]>mew[x+1]:
            fac(x,y)
fac(0,10)