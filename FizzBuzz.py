
min = int(input('[+] Please enter a MINIMUM number :> '))
max = int(input('[+] Please enter a MAXIMUM number :> '))

for num in range(min,max):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)