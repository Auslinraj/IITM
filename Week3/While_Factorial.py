#Find Factorail of a Number

print('Enter a Number: ')
n=int(input())

i=1
ans=1

while(i<=n):
  ans=ans*i
  i=i+1

print(ans)

#Find Factorial of a Number method 2

num=int(input('Enter the Number: '))
fact=1
if(num<0):
  print('Not defined')
else:
  while(num>0):
    fact=fact*num
    num=num-1
  print(fact)
