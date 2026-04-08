# factorial using recursion

def Fact(n):
    if(n==0 or n==1):
        return 1
    return n*Fact(n-1)

n = int(input("Enter number : "))

print(f"The factorial of {n} is {Fact(n)}")