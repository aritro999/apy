def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
print(GCD(num1, num2))