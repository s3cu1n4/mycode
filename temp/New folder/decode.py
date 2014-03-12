file_obj = open('temp/test2.txt','r')
s= file_obj.read()

open('temp/test3.txt','w').write(s)
