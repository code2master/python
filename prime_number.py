import math
def isPrime(num):
    for i in range(2,int(math.sqrt(num))):
        if(num%i==0):
            return False
    return True

print("is 13 prime number: ",isPrime(13))
print("is 28 prime number: ",isPrime(28))