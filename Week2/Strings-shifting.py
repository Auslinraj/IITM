#coding for letter shifting
alpha='abcdefghijklmnopqrstuvwxyz'
print(len(alpha))
print(alpha[0])

i=10
print(alpha[i])
print(alpha[i+1])
print(alpha[i+3])

i=25
print(alpha[i])
#print(alpha[i+1])
#print(alpha[i+3])

i=30
print(i%26)
print(alpha[i%26])


i=25
print(alpha[i])
print(alpha[i%26])
print(alpha[(i+3)%26])

a='auslin'
#make one letter shift
print(alpha.index(a[0]))
print((alpha.index(a[0])+1)%26)
print(alpha.index(a[0])%26)
print(alpha.index(a[1])%26)
print(alpha[(alpha.index(a[0])%26)])
print(alpha[(alpha.index(a[1])%26)])

b=''
b=b+(alpha[alpha.index(a[0])%26])
b=b+(alpha[alpha.index(a[0+1])%26])
b=b+(alpha[alpha.index(a[0+2])%26])
b=b+(alpha[alpha.index(a[0+3])%26])
b=b+(alpha[alpha.index(a[0+4])%26])
b=b+(alpha[alpha.index(a[0+5])%26])
print(b)

c=''
c=c+(alpha[(alpha.index(a[0])%26)+1])
c=c+(alpha[(alpha.index(a[0+1])%26)+1])
c=c+(alpha[(alpha.index(a[0+2])%26)+1])
c=c+(alpha[(alpha.index(a[0+3])%26)+1])
c=c+(alpha[(alpha.index(a[0+4])%26)+1])
c=c+(alpha[(alpha.index(a[0+5])%26)+1])
print(c)

#we can create an variable for no of shifts

d=''
k=2
d=d+(alpha[(alpha.index(a[0])%26)+k])
d=d+(alpha[(alpha.index(a[0+1])%26)+k])
d=d+(alpha[(alpha.index(a[0+2])%26)+k])
d=d+(alpha[(alpha.index(a[0+3])%26)+k])
d=d+(alpha[(alpha.index(a[0+4])%26)+k])
d=d+(alpha[(alpha.index(a[0+5])%26)+k])
print(d)