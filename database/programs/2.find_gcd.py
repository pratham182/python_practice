#find gcd(greatest common factor) of two no

def gcd(a,b):
    result= min(a, b)   #store min in result
    while(result):
        if a% result == 0 and b% result == 0:
            break
        result=result-1
    return result


#taking as two no as input from user
first=int(input("Enter the value of first no"))
second=int(input("Enter the value of second no"))

print(f"GCD of {first} and {second} is {gcd(first, second)}")