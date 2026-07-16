#1
'''print("Why can't a nose be 12 inches long? ")
input("Press Enter to see the answer...")
print("Because then it would be a foot!")'''


#2
'''date= int(input("Enter today's date: "))
days_left = 31 - date
print(days_left, "days are left in the month.")'''


#3
'''x=5
y=x*2
z=y-1
print(x)
print(y)
print(z)'''


#4
'''x=5
y=x*2
z=y-1
print(x,y,z,sep="@")'''


#5
'''n=5
a,b,c,d,e=n,2*n,3*n,4*n,5*n
print(a,b,c,d,e)'''


#6
'''radius=float(input("Enter radius of a circle: "))
area=3.14*radius*radius
print("The area of circle is:" , area)'''


#7
'''sub1=float(input("Enter marks of Comp: "))
sub2=float(input("Enter marks of Bio: "))
sub3=float(input("Enter marks of Chem: "))
sub4=float(input("Enter marks of Phy: "))
sub5=float(input("Enter marks of Eng: "))
avg=(sub1+sub2+sub3+sub4+sub5)/5
print("The average marks is: ",avg,"%")'''


#8
'''cm = float(input("Height in cm: "))
i = cm / 2.54
print(int(i/12), "feet",i%12, "inches")'''


#9
'''n=int(input("Enter the value of n: "))
print("The value of n²,n³,n⁴ are respectively ",n**2,n**3,n**4,sep=",")'''


#10
'''b = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))
print("Area =", 0.5 * b * h)'''


#11
'''p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = p * r * t / 100
ci = p * (1 + r/100) ** t - p
print("Simple Interest =", si)
print("Compound Interest =", ci)'''


#12
'''n = int(input("Enter a number: "))
print(n, 2*n, 3*n, 4*n, 5*n)'''


#13
'''name = input("Enter name: ")
cls = input("Enter class: ")
age = input("Enter age: ")

print(name, cls, age)
print("\n\n")
print(name)
print(cls)
print(age)'''


#14
'''n = int(input("Enter a digit: "))
print(n, n+1, n+2, sep="")'''


#15
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

a, b = a + b, b + c

print("a =", a)
print("b =", b)
print("c =", c)'''