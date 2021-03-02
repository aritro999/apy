x = int(input('Enter any number'))

y = (x // 2) + 1

per = 0

for num in range(1, y):

    if (x % num == 0):
        per = per + num

if per == x:
    print('Perfect No')
else:
    print('NoT Perfect No')