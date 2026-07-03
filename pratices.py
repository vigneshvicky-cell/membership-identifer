#python operators
'''
Arithemetic operators
Assigment operators
comparson operators
logical opearators
if
else
Btwise operators
identifiver operators
Membership operators'''


#Arithemetic operators
a=int(input("enter the number:"))
b=int(input("enter the second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#variable ku valu assiendpanurathu than assigment operator
a=b
print(a)
a-=b
print(a)
a+=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a%=b
print(a)
a**=b
print(a)
#comparson operator
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#Bitwise operator
c=6
d=7
print(c&d)
print(c|d)
print(c^d)
print(c<<d)
print(c>>d)
#logical operators (ethula ya if else pathudalam)
#and
i_d=input("you have id card""(yes/no)")
age=int(input("enter the age"))
if age>=18 and i_d=="yes":
    print("Allowed")
else:
    print("NOt allowed")
#or
a=int(input("enter you qualification:"))
if a==12 or a=="diploma":
    print("eligible")
else:
    print("not eligible")
#and+or
age=int(input("enter your age:"))
licensee=input("you have car or bike(car/bike):")
if age>=18 and licensee=="car" or licensee=="bike":
    print("Allow")
else:
    print("not allowed")
#and+not
fees=input("you pay your frees(yes/no):")
suspend=input("your susbend last week(yes/no):")
if fees=="yes" and suspend!="yes":
    print("aloweed")
else:
    print("not Aloowed")
#identifiver operator:
s=int(input("enter the mobile number:"))
v=int(input("enter the mobile number:"))
print(s is v)
print(s is not v)
print(id(s))
print(id(v))
#membership operator
name=input("enter your name:")
print("v" in name)
print("h"not in name)
