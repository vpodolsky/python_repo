PI = 3.14

type = input()
if (type == 'круг'):
    print(PI*int(input())**2)
elif (type == 'прямоугольник'):
    print(int(input())*int(input()))
elif (type == 'треугольник'):
    a,b,c = int(input()),int(input()),int(input())
    p = (a + b + c)/2
    print((p * (p - a) * (p - b) * (p - c))**0.5)

shape = input()

a = float(input())

if shape == "треугольник" or shape == "прямоугольник":
    b = float(input())
    S = a*b
    if shape == "треугольник":
        c = float(input())
        p = (a+b+c)/2
        S = (p*(p-a)*(p-b)*(p-c))**0.5
else:
    S = 3.14*a**2

print (S)