file1=open('file1.txt','r')
file2=open('file2.txt','r')
f2=file2.read()
while True:
    line = file1.readline()
    c=f2.count(line)
    if c == 0:
        print line,
    if line:
        pass
    else:
        break
    
