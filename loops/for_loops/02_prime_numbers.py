
# Program to check if a number is prime or not

n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i == 0):
        print(f"Number is not a prime number")
        break
else:
    print("Number is prime")