# HCF
def findHCF(a,b):

# choose the smaller number
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i       
    return hcf

num1 = 12
num2 = 18

# If you want to take input from user, uncomment below lines
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", findHCF(num1, num2))