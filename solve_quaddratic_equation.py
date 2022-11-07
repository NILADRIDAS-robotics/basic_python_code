# solve quadratic equation ax**2+bx+c

import cmath

a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))

d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print('the solution are {0} and {1}'.format(sol1,sol2))