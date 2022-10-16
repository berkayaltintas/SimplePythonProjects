
def square(k):
    print("Area of ​​the Square = {}".format(k*k))

def rectangular(k,u):
    print("Area of the Rectangular= {}".format(k,u))

def trapezoidal(x,y,z):
    print("Area of the Trapezodial ".format(((x+y)*z)/2))
def  parallelogram(a,b):
    print("Area of the Parallelogram = {}".format(a*b))
def equilateralquadrangle(m,n):
    print("Are of the Equilateral quadrangle={}".format((m*n)/2))

print(""" To inform:
1=Square 
2=Rectangular
3=Trapezodial
4=Parallelogram 
5=Equilateral quadrangle
""")
selection=int(input("The shape for which you want to calculate the area: "))

if (selection==1):
    k=int(input("One side of the sqaure:"))
    square(k)

elif (selection==2):
    k=int(input("short side of rectangle:"))
    u=int(input("long side of rectangle: "))
    rectangular(k,u)
elif (selection==3):
    x=int(input("Bottom base length of trapezoid:"))
    y=int(input("Length of the upper sole of the trapezoid:"))
    z=int(input("height of trapezoid:"))
    trapezoidal(x,y,z)
elif(selection==4):
    a=int(input("subbase length of parallelogram:"))
    b=int(input("height of parallelogram:"))
    parallelogram(a,b)
elif (selection==5):
    m=int(input("The length of the lower side of the rhombus:"))
    n=int(input("The length of the upper side of the rhombus"))
    equilateralquadrangle(m,n)
else:
    print("Please enter one of the suggested numbers.  ")