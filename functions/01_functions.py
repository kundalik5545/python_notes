'''
    Functions in python

    def funtionName(parameter):
        logical code goes here
    
    functionName()
    
'''

# def greet(name):
#     print(f"My name is {name}")

# greet("Kundalik")
# greet("Akshay")


# Another functions

shopName = "Ashok Shop"

def ShopName(shopName):
    print(f"My shop name is {shopName}")

ShopName("JK Kirana")
print(f"New shop is {shopName}")

# Global and local variable
# Always use global keyword infront of local variable if we want to access global variable in function 
# if there is no local variable present then no need to use global keyword

counter = 0

def Increment():
    global counter 
    # counter = 1
    counter = counter + 1
    print(f"Counter value inside func {counter}")

Increment()


# Local variable
# Local variable is can not be accessed outside of the function - Name error
def greet():
    message = "Hello"
    print(message)

greet()
# print(message)  # ❌ Error

# Tricky questions
print("🚀 Tricky Questions")

# If no local variable then no need to use global keyword
# If there is local variable then need to use global keyword
# for x = 20 we will get UnboundLocalError (common interview trap)

x = 10

def func(): 
    print(x)
    # x = 20


func()

# Local and global same variable - then no impact it will work
y = 10

def func2():
    y = 20
    print(y)

func2()
print(y)

# Nested function trick
print("🚀 Nested function trick")
def outer():
    x = 10
    def inner():
        # global x 
        x = 20
        print(f"inner x is {x}")
    inner()
    print(f"outer x is {x}")

outer()


# Nonlocal trick
print("🚀 Non local trick")
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        print(f"Inner x is {x}")
    inner()
    print(f"Outer x is {x}")

outer()

# Python LEGB rule
print("🚀 LEGB Rule of python")
x = "global"

def outer():
    x = "outer"
    def inner():
        print(x)
    inner()

outer()


# Interview tricky question
# we can define and initialize inside function also.
print("🚀 List created inside function as parameter")
def func(a=[]):
    a.append(1)
    return a

print(func())
print(func())
print(func())


'''
LEGB Rule - Local > Enclosing > Global > Built in
Nonlocal - This tell python ti use nearest enclosing local variable but not use global variable in any case
default paramerter - if we do not pass any parameter then it will take default parameter value
Return statement - it is used to return value from function and also to exit from function
'''

print("🚀 Return statement")
def Welcome(name):
    return f"Welcome {name}"

a = Welcome("Kundalik")
print(a)

print("🚀 Default parameter value")
def sum(a=10,b=20):
    return a + b

c = sum(35,34)
print(c)