#python basics
'''
1.comments
2.data type
3.variables
4.assigment
5.dynamic Typing
6.mutable&immutable
'''
#data type
name="vignesh"
age=22
CGPA=88.7
print(type(name))
print(type(age))
print(type(CGPA))
print("*"*(100))
#product
pn=input("enter the product name:")
p=float(input("enter the price:"))
q=int(input("enter the qunatity:"))
c=p*q
print("*"*(100))
print("product name:",pn)
print("product+qunatity",c)
print(type(pn))
print(type(p))
print(type(q))
print("*"*(100))
#percentage
names=input("student subject name :")
mark=float(input("enter the mark: "))
total_mark=("Percenntage",(name),mark*100)
print(total_mark)
print("*"*(100))
#slaray print
name1=input("enter the emplore name:")
age=int(input("enter the age:"))
salary=float(input("enter the salary:"))
print("NAME:",name1,"\nAGE:",age,"\nSALARY:",salary)
print(type(name1))
print(type(age))
print(type(salary))
print("*"*(100))
#car task
carname=input("enter the car name:")
model_year=int(input("enter the model year:"))
mileage=float(input("enter the mileage"))
print("CarName:",carname,"\nModelYear:",model_year,"\nMileage:",mileage)
#swaping(ethula enoru moadel kuda eruku c nu enoru variiable craet pani panala )
a=int(input("enter the a valu:"))
b=int(input("enter the b valu:"))
a,b=b,a
print(a,b)
#3(oru line la epudii multiple variables kudukalam nu pakalam:)
name,age,city="vicky",22,"salem"
print(name)
print(age)
print(city)
#epa oru vale epudii ellam variable kudukalam nu pakalam
a=b=c=100
print(a)
print(b)
print(c)

