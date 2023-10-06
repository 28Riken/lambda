#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(4, 5, 6))

#Lambda Functions
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(111))

#  Triples the number you send
def myfunc(n):
     return lambda a : a * n
mytripler = myfunc(3)
print(mydoubler(222))

# Both functions

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(22))
print(mytripler(33))