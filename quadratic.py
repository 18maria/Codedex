a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))

formula1 = -b + (b**2-(4*a*c))**0.5 /(2*a)
formula2 = -b-(b**2-(4*a*c))**0.5 /(2*a)

print(formula1)
print(formula2)