number=23
guess =int(raw_input('enter an integer : '))
if guess ==number:
    print 'congratulations, you guessed it.'# new block starts here
    print "(but you do not win any prizes!)"
elif guess < number:
    print 'no it is a little higer'
else:
    print 'no it is a litter lower'
    print 'Done'
