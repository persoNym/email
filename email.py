#! usr/bin/python
import re

str = raw_input("Enter Email >>> ")
if re.search('[a-zA-Z0-9+_\-\.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*(.[com]|[org]|[net]|[edu]|[mil]|[gov]|[biz]+)', str):
    print 'is a valid email format'
else:
    print 'is an invalid email format'