"""
#even odd 
num=int(input("pathukula number onu sollu"))
if num%2==0:
    print("even")
else:
    print("odd")
#2ahla divisible
a=int(input("ethachum nuber kudu"))
b=int(input("ethachum nuber kudu"))
if num%2==0 and  num%3==0:
    print("even")
else:
    print("odd")
#multiple
c=int(input("ethachum nuber kudu"))
d=int(input("ethachum nuber kudu"))
if c%5==0 and d%5==0:
    print("even")
else:
    print("odd")
"""
"""
#leap year
year=int(input("etha varusam sollu:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap yearb than kana :")
        else:
            print("leap yearv ella pa:")
    else:
        print("leap year than kanan :")
else:
     print("leap year ells pa ")
"""
"""
year=int(input("etha varusam sollu:"))
if year%4==0 and year%100!=0 or (year%400==0):
    print("leap year")
else:
    print("not leap year")
"""
"""
num=int(input("enter the number :"))
if num%4==0:
    if num%100==0:
        if num%400==0:
            print("leap year than pa")
        else:
            print("not leap year nanba")
    else:
        print("leap year than naba")
else:
 print("not leap year")
"""

stating_year=int(input("epo start ahgum sollu pa"))
ending_year=int(input("epo pa mudium pa"))
for  year in range(stating_year,ending_yeara):
    print (year)


