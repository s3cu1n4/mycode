number=23
running = True

while running:
    guess = int(raw_input("enter a integer:"))
    if guess == number:
        print "congratulations,you guessed it."
        running =False
    elif guess < number:
        print 'no, it is a little higher'
    else:
        print 'no,it is a little lower'
else:
    print 'the while loop is over.'
print 'done'
