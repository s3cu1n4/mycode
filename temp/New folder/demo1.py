import urllib
import sys
file_obj = open('temp/test2.txt','r')
s=file_obj.read()
s1=s.encode("utf-8")
utf8=urllib.quote(s1)
print utf8
