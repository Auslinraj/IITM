#different ways of printing and usage

pi=22/7
print('The value of PI =',pi)
print(f'The value of PI = {pi}')
print('The value of PI = {0}'.format(pi))
print('The value of PI = %d'%(pi))
print('The value of PI = %f'%(pi))

print(f'The value of PI = {pi:.2f}')
print('The value of PI = {0:.3f}'.format(pi))
print('The value of PI = %.4f'%(pi))


print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))


print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))