#normal print

country='India'
for letter in country:
  print(letter)


#formatted printing
#changing the default value of end (\n)

country='India'
for letter in country:
  print(letter,end=' ')
print(country)

for x in range(1,11):
  print(x,end=' ')
print(x)

#seperator

d=10
m=5
y=2021
print("Today's date is",d,m,y)
print("Today's date is",d,m,y,sep='/')
print("Today's date is")
print(d,m,y,sep='-')
print("Today's date is",end=' ')
print(d,m,y,sep='-')


#Different ways of printing
#normal printing

num=int(input())
for i in range(1,11):
  print(num,'x',i,'=',num*i)
  

#Format printing
num=int(input())
for i in range(1,11):
  print(f'{num}x{i}={num*i}')


#print using format function
num=int(input())
for i in range(1,11):
  print('{0}x{1}={2}'.format(num,i,num*i))


#old style of printing as like c lang
num=int(input())
for i in range(1,11):
  print('%dx%d=%d'%(num,i,num*i))
