#String Methods

x='python String'

#lower()
print(x.lower())
#upper()
print(x.upper())
#capitalize()
print(x.capitalize())
#title()
print(x.title())
#swapcase()
print(x.swapcase())
print('************')


#islower()
x='python'
print(x.islower())
x='Python'
print(x.islower())
x='PYTHON'
print(x.islower())
print('************')

#isupper()
x='PYTHON'
print(x.isupper())
x='Python'
print(x.isupper())
x='python'
print(x.isupper())
print('************')

#istitle()
x='python string method'
print(x.istitle())
x='Python String Method'
print(x.istitle())
x='Python string method'
print(x.istitle())
print('************')

#isdigit()
x='12345'
print(x.isdigit())
x='123abc'
print(x.isdigit())
x='abcd'
print(x.isdigit())
print('************')

#isalpha()
x='abc@#-'
print(x.isalpha())
x='123abc'
print(x.isalpha())
x='abcd'
print(x.isalpha())
print('************')

#isalnum()
x='abc@#-'
print(x.isalnum())
x='123abc'
print(x.isalnum())
x='abcd'
print(x.isalnum())
x='1234'
print(x.isalnum())
print('************')

#x='*-*-*-python-*-*-*'
x='-----python-----'
y='*-*-*-python-*-*-*'

#strip()
print(x.strip('-'))
print(y.strip('-'))
print(y.strip('*'))
print(y.strip('*-'))
print(y.strip('-*'))
print('************')

#lstrip()
print(x.lstrip('-'))
print(y.lstrip('-'))
print(y.lstrip('*'))
print(y.lstrip('-*'))
print(y.lstrip('*-'))
print('************')

#rstrip()
print(x.rstrip('-'))
print(y.rstrip('-'))
print(y.rstrip('*'))
print(y.rstrip('-*'))
print(y.rstrip('*-'))
print('************')

x='Python String Methods'

#count()
print(x.count('S'))
print(x.count('t'))
print('************')

#index()
'''index will search the specific leter from left
and 
gives us the first find as output'''
print(x.index('P'))
print(x.index('S'))
print(x.index('s'))
print('************')

#replace()
x=x.replace('P','p')
print(x)
x=x.replace('S','s')
print(x)
print('************')