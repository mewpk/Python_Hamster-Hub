mew=[]
def power(n,x):
    for z in range(1, x):
        mew.append(n*n)
        z +=1
    if z==x:
        print(sum(mew))
def sqroot(x):
    n = x**0.5
    print(n)
power(2,3)
sqroot(25)

