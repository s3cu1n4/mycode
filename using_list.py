shoplist=['apple','mango','carrot','banana']
print 'I have',len(shoplist),'items to purchase.'
print 'these items are:',
for item in shoplist:
    print item,
print '\nI also have to buy rice.'
shoplist.append('rice')
print 'my shopping list is now',shoplist
print 'I will sort my list now'
shoplist.sort()
print 'sorted shopping list is ',shoplist
print 'the first item I will buy is',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'b bought the ', olditem
print 'my shopeing list is now', shoplist
