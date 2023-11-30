#program to check whether a no prime or not
import math
 
def is_prime(n):
    #if n is less than or equal to 1 the return false
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
 
#taking no as a input from user
n=int(input("Enter the no"))


if(is_prime(n)==True): #prime
    print(f"{n} is prime")
else: #not a prime
    print(f"{n} is not prime")

