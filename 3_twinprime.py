def prime(n):
    f=0
    for i in range (2,(n//2)+1):
        if n%i == 0:
            f=1
            break
    return f
num=int(input("Enter starting number"))
num1=int(input("Enter last number"))
print("Twin prime numbers are")
for i in range(num,num1+1):
    if prime(i)== 0 and prime(i+2)==0:
        print(i," ",i+2)