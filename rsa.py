import random

def is_prime(n):
    """Check if a number is prime using a simple primality test."""
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    k = 0
    q = n - 1
    while q % 2 == 0:
        q >>= 1
        k += 1
    a = random.randint(2, n - 2)
    if pow(a, q, n) == 1:
        return True
    for j in range(k):
        if pow(a, 2 ** j * q, n) == n - 1:
            return True
    return False

def generate_large_prime():
    """Generate a large prime number with 20 digits."""
    while True:
        num = random.randrange(10**20, 10**21)
        if is_prime(num):
            return num

def generate_n():
    """Generate n = p * q, where p and q are large prime numbers."""
    p = generate_large_prime()
    q = generate_large_prime()
    t=(p-1)(q-1)
    return t

def find_privatekey(n):
    """Find e,the private key, such that gcd(e, n) = 1."""
    while True:
        e=random.randrange(2,n)
        if gcd(e,n)==1:
            return e

def gcd(a,b):
    #find gcd of 2 numbers
    while b!=0:
        a,b=b,a%b
    return a

def texttonumber(s):
    '''define a dictionary where each letter is mapped to a number. a should be
    mapped to 11, b to 12, and so on till z to 36. space should be mapped to
    37. A should be mapped to 38, B to 39, and so on till Z to 63.'''
    
    d={}
    t=''
    for i in range(26):
        d[chr(i+97)]=i+11
    d[' ']=37
    for i in range(26):
        d[chr(i+65)]=i+38
    for i in s:
        t+=str(d[i])
    return int(t)

def numbertotext(n):
    '''inverse of the above function.'''
    d={}
    for i in range(26):
        d[i+11]=chr(i+97)
    d[37]=' '
    for i in range(26):
        d[i+38]=chr(i+65)
    for i in range(10):
        d[i+1]=str(i)
    s=str(n)
    t=''
    for i in range(0,len(s),2):
        t+=d[int(s[i:i+2])]
    return t

def encrypt(p,e1,d2,n):
    #p is string. first convert it into a number using function texttonumber
    k=texttonumber(p)
    #encrypt the number as per rsa algorithm
    l=e1*d2
    c=pow(k,l,n)
    return c

def decrypt(c,d1,e2,n):
    #decrypt the number as per rsa algorithm
    l=d1*e2
    k=pow(c,l,n)
    #convert the decrypted number back to string using function numbertotext
    p=numbertotext(k)
    return p

def extended_gcd(e,t):
    #using extended euclidean algorithm find d such that e*d=1(mod t)
    a1=1
    a2=0
    a3=t
    b1=0
    b2=1
    b3=e
    while True:
        if b3==0:
            return None
        if b3==1:
            return b2
        q=a3//b3
        t1=a1-q*b1
        t2=a2-q*b2
        t3=a3-q*b3
        a1=b1
        a2=b2
        a3=b3
        b1=t1
        b2=t2
        b3=t3

def modinv(e,t):
    #find d using extended euclidean algorithm
    d=extended_gcd(e,t)
    return d

def main():
    #generate 2 20 digit prime numbers
    p=generate_large_prime()
    q=generate_large_prime()
    #calculate n
    n=p*q
    #calculate t
    t=(p-1)*(q-1)
    #find e
    e1=find_privatekey(t)
    e2=find_privatekey(t)
    if e1==e2:
        e2=find_privatekey(t)
    print(e1,e2)
    #find d
    d1=modinv(e1,t)
    d2=modinv(e2,t)
    #take input from user
    p=input("Enter the plain text:")
    #encrypt the plain text
    c=encrypt(p,e1,d2,n)
    print("The cipher text is:",c)
    #decrypt the cipher text
    p2=decrypt(c,d1,e2,n)
    #print the plain text
    print("The plain text is:",p2)
main()
