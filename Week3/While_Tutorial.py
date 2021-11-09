#Find no of digits in the given number

num=abs(int(input('Enter the Number:')))
digits=1
while(num>9):
  num=num//10
  digits=digits+1
print(digits)

#Reverse the digits of number

num=int(input('Enter the Number:'))
absnum=abs(num)
if(num>=0):
  rev=num%10
  num=num//10
  while(num>0):
    r=num%10
    num=num//10
    rev=rev*10+r
  print(rev)
else:
  rev=absnum%10
  absnum=absnum//10
  while(absnum>0):
    r=absnum%10
    absnum=absnum//10
    rev=rev*10+r
  print(rev-2*rev)

#reverse the digit of numbers given - another way

num=int(input('Enter the Number: '))
absnum=abs(num)
rev=absnum%10
absnum=absnum//10
while(absnum>0):
  r=absnum%10
  absnum=absnum//10
  rev=rev*10+r
if(num>=0):
  print(rev)
else:
  print(rev-2*rev)



#find whether given number is palindrome or not

num=int(input())
absnum=abs(num)
rev=absnum%10
absnum=absnum//10
while(absnum>0):
  r=absnum%10
  absnum=absnum//10
  rev=rev*10+r
if(num<0):
  rev=rev-2*rev
if(num==rev):
  print('Palindrome')
else:
  print('Not a Palindrome')

  