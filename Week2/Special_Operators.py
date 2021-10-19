#Multiple Assignment
x,y=1,2
print(x)
print(y)
print(x,y)

x=y=z=10
print(x)
print(y)
print(z)
print(x,y,z)
print('************')

#Reversing the Values
x,y=1,2
print(x,y)
x,y=y,x
print(x,y)
print('************')

#Deleting Variable
x=10
print(x)
del x
print('************')

#shorthand operators - Addition

count=0
count+=1
count+=1
count+=1
count+=1
print(count)

count=0
count+=1
count=count+1
print(count)
print('************')

#shorthand operators - Subraction

count=10
count-=1
count-=1
count-=1
count-=1
print(count)

count=10
count-=1
count=count-1
print(count)
print('************')

#shorthand operators - Multiplication

count=10
count*=2
count*=1
count*=2
count*=1
print(count)

count=10
count*=2
count=count*2
print(count)
print('************')

#shorthand operators - Division

count=10
count/=2
count/=1
count/=2
count/=1
print(count)

count=10
count/=2
count=count/2
print(count)
print('************')

#in operator
#It search the specific value in the given sentence, if yes then gives 'True' as output, if not, then gives 'False' as output

print('alpha' in 'An variable should habe alpha-numeric values')
print('alpha' in 'An variable should habe numeric values')
print('Alpha' in 'An variable should habe alpha-numeric values')
print('Alpha' in 'An variable should habe Alpha-numeric values')
print('************')