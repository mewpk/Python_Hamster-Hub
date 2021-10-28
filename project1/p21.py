mew=[]
def facto(n):
    for z in range(n,0,-1):
        mew.append(z)
        if z==1:
            for w in range(n-1,0,-1):
                mew[0]= w*mew[0]
                if w == 1:
                    print(mew[0])
facto(5)