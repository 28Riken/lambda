# Difference Between Lambda functions and def defined function
def cube(y):
    return y*y*y

lambda_cube = lambda y : y*y*y
print("Using function defined with 'def' keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))


# Python Lambda Function with List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

# Python Lambda Function with if-else
max = lambda a, b : a if(a>b)  else b

print(max(1, 2))

# Python Lambda with Multiple Statements
List = [[2,3,4],[1, 23, 10, 50],[3, 12, 5, 7]]
sortlist = lambda x : (sortlist(i) for i in x)

secondLargest = lambda x, f : [y[len(y)-2]for y in f(x)]
res = secondLargest(List, sortlist)

print(res)


# Filter out all odd numbers using filter() and lambda function
li = [5, 6, 12, 58, 6, 23, 78 ,32, 65, 77]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# Filter all people having age more than 18, using lambda and filter() function
ages = [12, 90, 17, 59, 60, 5]
adults = list(filter(lambda age: age > 10, ages))

print(adults)

# Using lambda() Function with map()
li = [5, 7, 23, 45, 67, 32, 23, 90]

final_list = list(map(lambda x: x*2, li))
print(final_list)

# Transform all elements of a list to upper case using lambda and map() function
animals = ['dog', 'cat', 'parrot', 'fish']
uppered_animals = list(map(lambda animal: animal.upper(), animals))
print(uppered_animals)

# A sum of all elements in a list using lambda and reduce() function
from functools import reduce
li = [4, 5 ,67, 12, 34, 20, 40]
sum = reduce((lambda x, y: x + y), li)
print(sum)

# Find the maximum element in a list using lambda and reduce() function
import functools

lis = [1, 2, 3, 4, 5, 6]
print("The maximum elment of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

