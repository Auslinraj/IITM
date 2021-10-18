#Accept five words as input and print the sentence formed by these words after adding a space between consecutive words and a full stop at the end
a1=str(input())
a2=str(input())
a3=str(input())
a4=str(input())
a5=str(input())
b=(a1+' '+a2+' '+a3+' '+a4+' '+a5+'.')
print(b)

#Accept the date in DD-MM-YYYY format as input and print the year as output.
date=input()
year=date[-4:]
print(year)

#Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers
single=input()
d1=int(single[0])
d2=int(single[2])
d3=int(single[4])
d4=int(single[6])
d5=int(single[8])
d=d1*d2*d3*d4*d5
print(d)

#Assume that several IITs start offering online degrees across multiple branches
email=input()
branch=email[0:2]
degree=email[3:5]
year=email[6:8]
rollnumber=email[9:13]
Institute='iitm'
print(branch)
print(degree)
print(year)
print(rollnumber)
print(Institute)


#Accept two positive integers x and y as input. Print the number of digits in x power y
x=int(input())
y=int(input())
z=x**y
z_str=str(z)
print(len(z_str))


#Accept two positive integers M and N as input. There are two cases to consider: (1) If M < N, then print M as output. (2) If M >= N, subtract N from M. Call the difference M1. If M1 >= N, then subtract N from M1 and call the difference M2. Keep doing this operation until you reach a value k, such that, Mk < N. You have to print the value of Mk as output.
M = int(input())
N = int(input())
print(M % N)

