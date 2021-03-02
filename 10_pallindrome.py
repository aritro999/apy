def f1(num):
    temp = num
    reverse = 0
    while num > 0:
        last_dig = num % 10
        reverse = reverse * 10 + last_dig
        num = num // 10

    if temp == reverse:
        print("The number is palindrome!")
    else:
        print("The number is not a palindrome!")


num = int(input("Enter a number: "))
f1(num)