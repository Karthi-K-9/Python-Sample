num = int(input('Enter a number : '))
fibonacci = [0, 1]
while num > fibonacci[-1]:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
if num in fibonacci:
    print('{} is a fibonacci number '.format(num))
else:
    print('{} is not a fibonacci number '.format(num))

