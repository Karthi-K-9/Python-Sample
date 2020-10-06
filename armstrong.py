num = int(input('Enter number : '))
num1 = num
total = 0
while num1 > 0:
    i = num1 % 10
    total = total + (i ** 3)
    num1 = num1//10
if num == total:
    print('{} is an Armstrong number '.format(num))
else:
    print('{} is not an Armstrong number '.format(num))







