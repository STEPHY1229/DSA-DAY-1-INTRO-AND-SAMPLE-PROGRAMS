#write a code to check whether the number is even or odd
'''num = int(input("enter a number:"))
print(num)
if num % 2 == 0:
    print("the number is even",num)
else:
    print("the number is odd",num)
    
#write a code to check the greatest among two numbers with user defined
num1 = int(input("num1="))
num2 = int(input("num2="))
print(num1)
print(num2)
if num1 > num2:
    print(num1,"is greater")
else:
    print(num2,"is greater")
    
    
#write a code to check whether the number is positive or negative or zero
num = int(input("enter a number:"))
if num > 0:
    print(num,"is a positive number.")
if num < 0:
    print(num,"is a negative number.")
if num == 0:
    print(num,"is the given number")
    
#write a code to check who is taller among three
manju = float(input("Enter height of MANJU:"))
hani = float(input("Enter height of HANI:"))
babloo = float(input("Enter height of BABLOO:"))
if (manju > hani) and (manju > babloo):
    print("MANJU is taller than HANI and BABLOO")
elif (hani > manju) and (hani > babloo):
    print("HANI is taller than MANJU and BABLOO")
else:
    print("BABLOO is taller than MANJU and HANI")
    
#write a code to print n natural numbers
n = int(input("Enter the value of n:"))
l = 1
while l<=n:
    print(l,end= ',')
    l += 1 
    
    
#write a code to print even numbers
n = int(input("Enter the value of n:"))
l = 0
while l<= n:
    if (l%2==0):
        print(l,end=',')
    l += 1 
    
#write a code to print odd numbers
n = int(input("Enter the value of n:"))
l = 0
while l<= n:
    if (l%2==1):
        print(l,end=',')
    l += 1 
    
#write a code to print sum of n even numbers
n = int(input("Enter the value of n:"))
l = 1 
s = 0
while l<= n:
    if (l%2==0):
        s += l
    l += 1 
print("sum of n even numbers is",s)'''

#.write a code to print sum of digits of a given number by user
'''n = int(input("Enter digits to get their sum:"))
s = 0
while n != 0:
    digit = n%10
    s += digit
    n = n // 10
    
print("sum of digits is:",s)'''

#write a code to print the reverse of digits
'''n = int(input("Enter a number:"))
r = 0
while n!=0:
    d=n%10
    r=(r*10)+d 
    n=n//10
print("the reverse of",n,"is",r)'''

#write a code to check whether a given number is palindrome or not.
'''n = int(input("Enter a number:"))
t=n 
r = 0
while n!=0:
    d=n%10
    r=(r*10)+d 
    n=n//10
if t == r:
    print(t,"is a palindrome number")
else:
    print(t,"is not a palindrome number")'''

#write a code to check whether a given number is armstrong or not.    
'''n = int(input("Enter a number:"))
c = n
p = len(str(n))
r = 0
while n!=0:
    d=n%10
    r += d**p  
    n=n//10
if r == c:
    print("armstrong")
else:
    print("not armstrong")'''
    
