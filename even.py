def even():
    num = int(input('Enter the number:\n'))
    if num % 2 == 0:
        print(num,'Even number',sep=' : ')
    else:
        print(num,'Odd number',sep=' : ')
even()