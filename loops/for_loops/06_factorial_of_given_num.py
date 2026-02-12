
# Find the factorial of a given number

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1): 
    fact = i * fact
print(f"factorial of given number {n} is {fact}")


'''
5! = 1 X 2 X 3 X 4 X 5

fact(1) = 1
fact(2) = 1 X 2 = 2
fact(3) = 1 X 2 x 3 = 6
'''