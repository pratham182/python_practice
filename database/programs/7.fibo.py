#print fibonacci series 

def fibo(n):
    #base case
    if n<=1:
        return n
    #recursive relation
    return fibo(n-1)+fibo(n-2)

#taking n from the user
n=int(input("Enter the value of n"))

print("Fibonacci series",end=" ")
for i in range(n):
    print(fibo(i),end=" ")
print(" ")