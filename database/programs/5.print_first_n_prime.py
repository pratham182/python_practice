#Program to print first n prime no

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Input the value of N from the user
N = int(input("Enter the value of N: "))


prime_numbers = generate_primes(N)
print(f"The first {N} prime numbers are: {prime_numbers}")
