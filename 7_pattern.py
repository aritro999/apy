n = int(input("Enter the rows: "))
count = 1


def f1(count):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count % 2, end=" ")
            count += 1
        print()
        if (i % 2 == 0):
            count = 1
        else:
            count = 0


f1(n)