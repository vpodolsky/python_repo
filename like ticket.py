a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')

a=int(input())
a1=a%10
a2=(a%100)//10
a3=(a%1000)//100
a4=(a%10000)//1000
a5=(a%100000)//10000
a6=a//100000
if a1+a2+a3==a4+a5+a6:
    print('Счастливый')
else:
    print('Обычный')