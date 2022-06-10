#1
name="Rajiv Gandhi University of Knowledge Technologies"
print(name)

#2
p=int(input("Enter initial principal balance:"))
r=float(input("Enter annual intrest rate:"))
t=int(input("Enter time in years:"))
n=int(input("Enter the number of times:"))
#simple intrest
si=p*(1+r*t)
print("Simple Interest:",si)
#compound intrest
ci=p*(1+(r/n))**(n*t)
print("Compound Interest:",ci)

#3
watts=int(input("Enter watts:"))
time=int(input("Enter time in days:"))
time=time*24
kwh=watts*time
print("Total Bill:",kwh,"watts/hour")



#4
x1=int(input("Enter the value of x1:"))
x2=int(input("Enter the value of x2:"))
y1=int(input("Enter the value of y1:"))
y2=int(input("Enter the value of y2:"))
d=((x2-x1)**2 + (y2-y1)**2)**0.5
print("the distance between two points :",d)

#5
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
sum=num1+num2
print("Total Sum:",sum)

#6
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
num3=int(input("Enter number3:"))
avg=(num1+num2+num3)/3
print("Average of Three Numbers:",avg)

#7
a=int(input("Enter a:"))
b=int(input("Enter b:"))
x=int(input("Enter x:"))
exp=(a*x+b)/(a*x-b)
print(exp)

#8
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))

temp=num1
num1=num2
num2=temp
print("After swapping:\n Num1:",num1," Num2:",num2)

#9
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After swapping:\n Num1:",num1," Num2:",num2)

#10

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
#calculate discriminant
d=(b**2)-(4*a*c)
#finding two sol
sol1=-b+(d**0.5)/2*a
sol2=-b-(d/2*a)**0.5
print("The Solutions are {} and {} ".format(sol1,sol2))



























