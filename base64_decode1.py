import base64
file_obj = open('temp/test.txt','r')
s= file_obj.read()
a=base64.decodestring(s)
print a
