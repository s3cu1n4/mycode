import base64
 
filea = open(r'temp\test.txt','r')   
lines = filea.readlines()
writefile=open(r'temp\test1.txt','w')
for i in lines:   
        word = i.strip()
        b = base64.decodestring(word)
        print b
        writefile.write(b)
        writefile.write('\n')
writefile.close()
filea.close()
