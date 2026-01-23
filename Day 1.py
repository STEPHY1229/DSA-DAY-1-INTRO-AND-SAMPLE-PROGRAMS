'''#1.write a code to print sum of digits of a given number by user

num = int(input("Enter a number to print sum of digits:"))
summ = 0
while num != 0:
    digit = num%10
    summ += digit
    num = num // 10

print("sum of digits :",summ)

#2.reverse of a user_defined number

num = int(input("Enter a number for reverse:"))
rev = 0
while num != 0:
    digit = num % 10
    rev = (rev*10) + digit
    num = num // 10
print("reverse of a number:",rev)

#3.palindromic of a user_defined number without temporary variable it is not possible.

num = int(input("Enter a number to check palindromic:"))
tem = num 
rev = 0
while num != 0:
    digit = num % 10
    rev = (rev*10) + digit
    num = num // 10

if tem == rev:
    print(rev,"is a palindromic number")
else:
    print(rev,"is not a palindromic number")

#4.ARM STRONG number

n = int(input("Enter a number to check armstrong:"))
cop = n
summ = 0
while n !=0:
    summ += digit**3
    n = n // 10
if summ == cop:
    print(cop,"is an armstrong number")
else:
    print(cop,"is not an armstrong number")'''

'''#5. Niven's number

n1 = int(input("Enter a number to check Niven or not:"))
cop1 = n1
summ = 0
while n1!=0:
    r = n1 % 10
    summ += r
    n1 = n1 // 10

if cop1 % summ == 0:
    print(cop1,"is a niven number")
else:
    print(cop1,"is not a niven number")'''
              
#6. strong number

num = int(input("Enter a number to check strong number:"))
cop = num
summ = 0
while num!=0:
    digit = num%10
    f = 1
    i = 1
    while i <= digit:
        f = f*i
        i += 1
    summ += f
    num = num // 10

if cop == summ:
    print(cop,"is a strong number")
else:
    print(cop,"is not a strong number")

#7.
    













