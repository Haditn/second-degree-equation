# solving the equation of ax^2+bx+c=0:
    
#importing the needed libraries
import math as m

#asking for the equation's constants
a= float(input("please enter value of a:"));
b= float(input("please enter value of b:"));
c= float(input("please enter value of c:"));

#measuring the delta:    
D= pow(b, 2)-(4*a*c);

if D>0:
    x_1=(-b+(m.sqrt(D)))/(2*a);
    x_2=(-b-(m.sqrt(D)))/(2*a);
    print("X1= ",x_1);
    print("X2= ",x_2);
elif D==0:
    x=(-b)/(2*a);
    print("X= ",x);
else:
    print("the equation can not be solved.")