def printmax(x,y):
    '''prints the maximum of two numbers.
        the two values must be integers.'''
    x=int(x)
    y=int(y)
    if x>y:
        print x,'is m'
    else:
        print y,'is m'
printmax(3,5)

print printmax.__doc__
help(printmax)
