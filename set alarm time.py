x=int (input())
H=int (input())
M=int (input())
y=(x/60)
t=int(y)
z=round((y-t)*60)
A =(H+t)
B= (M+z)
if B < 60:
    print (A)
    print (B)
else:
    b=(B-60)
    A=(H+t+1)
    print (A)
    print (b)