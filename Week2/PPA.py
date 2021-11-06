#Accept a non-zero integer as input. Print positive if it is greater than zero and negative if it is less than zero

num=int(input())
if num>0:
  print('positive')
else:
  print('negative')


#accept float value

x=float(input())
a=x+2
b=(x*x)+2
c=0
if(x>0 and x<10):
  print(a)
elif(x>=10):
  print(b)
else:
  print(c)


#accept int as input and print the time of the day.

T=int(input())
if (T>=0 and T<=23):
  if(T>=0 and T<=5):
    print('NIGHT')
  elif(T>=6 and T<=11):
    print('MORNING')
  elif(T>=12 and T<=17):
    print('AFTERNOON')
  elif(T>=18 and T<=23):
    print('EVENING')
else:
  print('INVALID')


#accept 2D space as input and get the output as axis, origin or quadrant.

x=float(input())
y=float(input())
if(x>0 and y>0):
  print('first')
elif(x>0 and y<0):
  print('fourth')
elif(x<0 and y<0):
  print('third')
elif(x<0 and y>0):
  print('second')
elif(x==0 and y==0):
  print('origin')
elif(x==0 and y>=0):
  print('y-axis')
elif(x==0 and y<=0):
  print('y-axis')
elif(y==0 and x>=0):
  print('x-axis')
elif(y==0 and x<=0):
  print('x-axis')


#Accept a string as input. If the input string is of odd length, then continue with it. If the input string is of even length, make the string of odd length as below:

word=input()
w=len(word)
wl=w%2
wi=w/2
wi=int(wi)
#print(wi)
ww=(word[-1])
if(wl==0 and ww=='.'):
  #if(word[-1]==.)
  #ww=(word[-1])
  www=(word[0: -1])
  www=len(www)
  www=www/2
  www=int(www)
  wwww=(word[www-1])
  wwww=wwww+(word[www])
  wwww=wwww+(word[www+1])
  print(wwww)

  #if(ww==.)
  #  print(word[0: -1])
  #print(ww)
  #print(word[0: ])
  #if(word[-1] is .)
  #  print(ww)
  if(wl==0 and ww!='.'):
    wo=word+'.'
    print(wo)
    wol=len(wo)
    wol=wol/2
    wol=int(wol)
    #print(wol)
    final=(wo[wol-1])
    final=final+(wo[wol])
    final=final+(wo[wol+1])
    print(final)
  #print(wo[wol-1])
  #print(wol)
else:
  final=(word[wi-1])
  final=final+(word[wi])
  final=final+(word[wi+1])
  print(final)

  