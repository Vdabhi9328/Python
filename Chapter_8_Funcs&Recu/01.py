# using function find greatest of three

a = int(input("Enter number : "))
b = int(input("Enter number : "))
c = int(input("Enter number : "))

def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
print(greatest(a,b,c))



#