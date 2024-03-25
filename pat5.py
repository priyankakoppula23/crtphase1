n=4
a=n
b=n
for i in range(1,n+1):
    for j in range(1,n*2):
        if j==a or j==b or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    a-=1
    b+=1
    print()