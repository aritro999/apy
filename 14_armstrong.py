Num = int(input("\nPlease Enter the Number to Check for Armstrong: "))


def Armstrong_Number(Num):
    Sum = 0
    Times = 0

    Temp = Num
    while Temp > 0:
        Times = Times + 1
        Temp = Temp // 10

    Temp = Num
    for n in range(1, Temp + 1):
        Reminder = Temp % 10
        Sum = Sum + (Reminder ** Times)
        Temp //= 10
    return Sum


if (Num == Armstrong_Number(Num)):
    print("\n %d is Armstrong Number.\n" % Num)
else:
    print("\n %d is Not a Armstrong Number.\n" % Num)