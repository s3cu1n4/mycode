ab={'swaroop':'swaroopch@byreofpython.info',
    'larry'  :'larry@wall.org',
    'mastumoto':'maasdf@java.org',
    'sp':'spm@hotmail.com'
    }
print "swaroot's address is %s" % ab['swaroop']
ab['guido']='guido@python.org'
del ab['sp']
print '\n ab is len=',len(ab)
for name,address in ab.items():
    print 'contact %s at %s' %(name,address)
if 'guido' in ab:
    print "\nguido's addres is %s" %ab['guido']
