# n=int(input("enter:"))
def f(n):
   
    if n==0:
        return 1
    return n*f(n-1)
# a=f(n)
a=f(5)
# f(n)
f(5)
print(a)