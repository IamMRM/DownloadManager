from urlparse import urlparse

o = urlparse('http://www.example.com/myfile.png')
print o.netloc
print o.path