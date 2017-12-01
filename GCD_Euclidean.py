# HCF
# Using Eucid algorithm for calculating gcd
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
num1 = 12
num2 = 18

# If you want to take input from user, uncomment below lines
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", gcd(num1, num2))