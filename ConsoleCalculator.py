from math import sqrt


while True:
    try:
        print('Use (+,-,/,*,**, >, <, =, !, sqrt()) as operators')
        cos = input('Type in the equation or press ENTER to exit: ')
        if cos=='':
            break
        else:
            print(f'{cos} equals {eval(cos)}')
    except:
        print('Something went wrong.')