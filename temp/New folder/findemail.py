file_obj =open('temp/tcl.txt','r')
s =file_obj.read()
user = ['']*200
i=0
email = s.find(r'"Email">')    
tcl = s.find(r'@tcl.com')
while i< 200:
    user[i] = s[email + 8:tcl + 8]
    print user[i]
    email = s.find(r'"Email">',tcl)    
    tcl = s.find(r'@tcl.com',email)    
    i = i+1  
else:
    print 'find end!'
