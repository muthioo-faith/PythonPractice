from binascii import b2a_hqx


def add(a,b):
    answer=a+b
    return answer

def subtract(a,b):
    answer=a-b
    return answer

def multiply(a,b):
    answer=a*b
    return answer

def divide(a,b):
    answer=a/b
    return answer

def modulus(a,b):
    answer=a%b
    return answer

def intdivide(a,b):
    answer=a/b
    return answer

def exponent(a,b):
    answer=a**b
    return answer

def square(a):
    answer=a*a
    return answer

def cube(a):
    answer=a*a*a
    return answer

def factorial(a):
    fact=1
    for num in range(1,a+1):
      fact*=num
    return fact

