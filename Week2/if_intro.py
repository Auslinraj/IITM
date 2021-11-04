#intro to if statement
#find the age to watch movie
print('Enter your year of birth:')
birth_year=int(input())

current_year=2021

age=current_year-birth_year

if(age<13):
  print('you are under age')
  print('wait until old enough')
else:
  print('you are old enough')
  print('enjoy')

print('Have a nice time')
print('************')

#Find given number is odd or even

num=int(input('Enter the number: '))
if(num%2==0):
  print("Even")
else:
  print('Odd')


#Find the given number ends with 0 or 5

num=int(input('Enter the number: '))
if(num%5==0):
  if(num%10==0):
    print('0')
  else:
    print('5')
else:
  print('Other')


#Find the grade based on marks.

marks=int(input('Enter the Marks: '))
if(marks>=0 and marks<=100):
  if(marks>=90):
    print('A')
  if(marks>=80 and marks<90):
    print('B')
  if(marks>=70 and marks<80):
    print('C')
  if(marks>=60 and marks<70):
    print('D')
  if(marks<=60):
    print('E')
else:
  print('Invalid Input')


