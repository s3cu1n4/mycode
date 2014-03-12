import base64
file_obj =open('temp/test.txt','r')
s =file_obj.read()
user = ['']*100
i=0
email = s.find(r'<response base64="true"><![CDATA')    
tcl = s.find(r'></response>')
while email != -1 and tcl != -1 and i< 100:
    user[i] = s[email + 32:tcl -1]
#    print user[i]
    t=base64.decodestring(user[i])
    s=t.read()
    print t
    open('temp/test2.txt','w').write(t)
    email = s.find(r'<response base64="true"><![CDATA',tcl)    
    tcl = s.find(r'></response>',email)    
    i = i+1  
else:
    print 'find end!'


