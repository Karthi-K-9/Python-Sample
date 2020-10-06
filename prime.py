num1 = int(input('Enter start point : '))
if num1 < 0:
    print('Enter a value greater than 0')
    exit()
num2 = int(input('Enter end point : '))
if num2 <= num1:
    print('End should be greater than start')
    exit()
for i in range(num1, num2 + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)



