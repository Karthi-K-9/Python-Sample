principle = int(input('Enter Principle : '))
if principle <= 0:
    print('Principle should be greater than 0')
    exit()
interest_rate = float(input('Enter rate of interest : '))
if interest_rate <= 0:
    print('Rate of interest should be greater than 0')
    exit()
time = float(input('Enter time in years : '))
if time <= 0:
    print('Time should be greater than 0')
    exit()
interest = (principle * interest_rate * time) // 100
print('Interest is ' + str(interest))
