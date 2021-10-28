mew=[]
n =0
def fac(x):
    global n 
    n = n+1
    if n==1:
        mew.append(x)
    if x>1:
        factoo(x-1)
    else: print(mew)
def factoo(x):
    mew[0]=mew[0]*x
    fac(x)
fac(5)
