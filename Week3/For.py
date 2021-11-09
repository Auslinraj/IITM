#for loop

for i in range(5):
  print(i,'Hello')

for i in range(5):
  print(i,'abcd')
  print(i,'1234')


n=int(input('Enter a Number: '))
for i in range(n):
  if(i%2==0):
    print(i,'yes')
  else:
    print(i,'No')


#add first n numbers - for loop

n=int(input('Enter the Value: '))
sum=0
for i in range(n):
  sum=sum+i
print(sum)

#multiplication Table - For loop

for i in range(1,11):
  print('2x',i,'=',2*i)



