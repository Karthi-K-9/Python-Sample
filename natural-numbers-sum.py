num = int(input('Enter a natural number '))
if num <= 0:
    print('{} is not a natural number'.format(num))
    exit()
total = 0
for i in range(1, num+1):
    total = total + i

# total = (num * (num + 1)) // 2         --this can replace lines 5 through 7

print('Sum of first {} natural numbers is {}'.format(num, total))

