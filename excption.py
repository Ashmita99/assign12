#question 1
#define Python user-defined exception
class Error(Exception):
"""Base class for other exceptions"""
pass
class AgeTooSmallError(Error):
"""Raised when the entered age is smaller than 18"""
pass
while True:
try:
age = input("Enter Age: ")
if age < 18:
raise AgeTooSmallError
break
except AgeTooSmallError:
print("The entered Age is too small, try again!")
print('')
print("You entered the appropriate age value!")

#questn2

IndexError
----------------------------------------------------------
-----------------
IndexError Traceback (most recent call last)
<ipython-input-6-ea9ef666f953> in <module> ()
1 l =[ 1 , 2 , 3 ]
----> 2 print ( l [ 3 ])
IndexError : list index out of range
# Python program to handle simple runtime error
a = [ 1 , 2 , 3 ]
try :
print ( "Second element = %d" %(a[ 1 ]))
# Throws error since there are only 3 elements in array
print ( "Fourth element = %d" %(a[ 3 ]) )
except IndexError:
print ( "An error occurred" )s

#question3
IndexError
----------------------------------------------------------
-----------------
IndexError Traceback (most recent call last)
<ipython-input-6-ea9ef666f953> in <module> ()
1 l =[ 1 , 2 , 3 ]
----> 2 print ( l [ 3 ])
IndexError : list index out of range
# Python program to handle simple runtime error
a = [ 1 , 2 , 3 ]
try :
print ( "Second element = %d" %(a[ 1 ]))
# Throws error since there are only 3 elements in array
print ( "Fourth element = %d" %(a[ 3 ]) )
except IndexError:
print ( "An error occurred" )


#question4

IndexError
----------------------------------------------------------
-----------------
IndexError Traceback (most recent call last)
<ipython-input-6-ea9ef666f953> in <module> ()
1 l =[ 1 , 2 , 3 ]
----> 2 print ( l [ 3 ])
IndexError : list index out of range
# Python program to handle simple runtime error
a = [ 1 , 2 , 3 ]
try :
print ( "Second element = %d" %(a[ 1 ]))
# Throws error since there are only 3 elements in array
print ( "Fourth element = %d" %(a[ 3 ]) )
except IndexError:
print ( "An error occurred" )

#question5



#define Python user-defined exception
class Error(Exception):
"""Base class for other exceptions"""
pass
class AgeTooSmallError(Error):
"""Raised when the entered age is smaller than 18"""
pass
while True:
try:
age = input("Enter Age: ")
if age < 18:
raise AgeTooSmallError
break
except AgeTooSmallError:
print("The entered Age is too small, try again!")
print('')
print("You entered the appropriate age value!")



