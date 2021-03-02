def prime():
    num = int(input("enter a number"))
    f=0
    for i in range(2 ,int(num/2)+1):
        if num % i == 0:
            f = 1
            break
    if f == 0:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
prime()