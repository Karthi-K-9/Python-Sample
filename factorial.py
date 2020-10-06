num = int(input('Enter number : '))
fact = 1
if num < 0:
    print("Can't find factorial of negative number")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of {} is  {}".format(num, fact))

