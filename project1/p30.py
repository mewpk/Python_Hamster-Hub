mew = [12,45,8,6,5]
pp = [1]
def lol(x):
    if 0 <x:
        op(x)
def op(x):
    if mew[x]<mew[x+1]:
        lol(x+1)
    elif mew[x]>mew[x+1]:
        pp[0]=mew[x+1]
        mew[x+1] = mew[x]
        mew[x] = pp[0]
        lol(x+1)

