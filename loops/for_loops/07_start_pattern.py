''' 
Star Pattern
*
**
***
****
'''
n = int(input("Enter the number of rows: "))

print("Star Pattern")

for i in range(1,n +1): 
    stars = "*" * i
    print(stars)



''' 
Star Pattern
  *
 ***
*****

'''

print("Star Pattern")

for i in range(1,n +1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) 


''' 
Star Pattern
***
* *
***

'''

print("Star Pattern")

for i in range(1, n + 1):
    if(i == 1 or i == n):
        print("*" * (n), end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")