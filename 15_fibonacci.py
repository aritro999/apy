def f1(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input("enter a number"))
f1(n)