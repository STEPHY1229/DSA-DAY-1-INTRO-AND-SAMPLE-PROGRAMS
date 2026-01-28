#1.write a code to print sum of digits of a given number by user

num1 = int(input("Enter a number to print sum of digits:"))
summ1 = 0
while num1 != 0:
    digit = num1%10
    summ1 += digit
    num1 = num1 // 10

print("sum of digits :",summ1)

#2.reverse of a user_defined number

num2 = int(input("Enter a number for reverse:"))
rev = 0
while num2 != 0:
    digit = num2 % 10
    rev = (rev*10) + digit
    num2 = num2 // 10
print("reverse of a number:",rev)

#3.palindromic of a user_defined number without temporary variable it is not possible.

num3 = int(input("Enter a number to check palindromic:"))
tem = num3 
rev3 = 0
while num3 != 0:
    digit = num3 % 10
    rev3 = (rev3*10) + digit
    num3 = num3 // 10

if tem == rev3:
    print(rev3,"is a palindromic number")
else:
    print(rev3,"is not a palindromic number")

#4.ARM STRONG number (153 = 1^3 + 5^3 + 3^3 = 1+120+27 = 153)

n = int(input("Enter a number to check armstrong:"))
cop = n
summ = 0
while n !=0:
    summ += digit**3
    n = n // 10
if summ == cop:
    print(cop,"is an armstrong number")
else:
    print(cop,"is not an armstrong number")

#5. Niven's number (156 = 1+5+6 = 12; 156/12=0)

n1 = int(input("Enter a number to check Niven or not:"))
cop1 = n1
summ5 = 0
while n1!=0:
    r = n1 % 10
    summ5 += r
    n1 = n1 // 10

if cop1 % summ5 == 0:
    print(cop1,"is a niven number")
else:
    print(cop1,"is not a niven number")
              
#6. strong number (145 = 1! + 4! + 5! = 1+24+120 = 145)

num6 = int(input("Enter a number to check strong number:"))
cop6 = num6
summ6 = 0
while num6!=0:
    digit = num6%10
    f = 1
    i = 1
    while i <= digit:
        f = f*i
        i += 1
    summ6 += f
    num6 = num6 // 10

if cop6 == summ6:
    print(cop6,"is a strong number")
else:
    print(cop6,"is not a strong number")

#7. #write a code to print n natural numbers
n = int(input("Enter the value of n:"))
l = 1
while l<=n:
    print(l,end= ',')
    l += 1 
    
#8.write a code to print even numbers
n = int(input("Enter the value of n:"))
l = 0
while l<= n:
    if (l%2==0):
        print(l,end=',')
    l += 1 
    
#9.write a code to print sum of n even numbers
n = int(input("Enter the value of n:"))
l = 1 
s = 0
while l<= n:
    if (l%2==0):
        s += l
    l += 1 
print("sum of n even numbers is",s)

#10.write a code to print sum of n odd numbers
n = int(input("Enter the value of n:"))
l = 1 
s = 0
while l<= n:
    if (l%2==1):
        s += l
    l += 1 
print("sum of n odd numbers is",s)










