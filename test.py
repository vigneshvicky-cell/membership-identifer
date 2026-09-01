#palindrom
# num = int(input("Enter the value:"))
# original=num
# reversed=0

# while num>0:
#     digith=num%10
#     reversed=reversed*10+digith
#     num=num//10

# if original==reversed:
#     print("palindrom")

# else:
#     print("not palindrom")

#amstrong

# num  = int(input("Enter the number:"))
# digiths=len(str(num))
# orginal=num
# reversed=0


# while num>0:
#     digith=num%10
#     reversed=reversed+digith**digiths
#     num=num//10



# if reversed==orginal:
#     print("Amstrong")



# else:
#     print("NOT Amstrong")


#spy number
# num=int(input("Eneter the number :"))
# eno=num
# cno=0
# mno=1

# while num>0:
#     digith=num%10
#     cno=cno+digith
#     mno=mno*digith
#     num=num//10


# if cno==mno:
#     print("spy number")

# else:
#     print("Not a spy number ")

num = int(input("enter nuber :"))
while num >10:
    pro=1

    while num>0:
        digth=num%10
        pro=pro*digth
        num=num//10
    num=pro

if num==1:
    print("hash number:")

else:
    print("not a hash number")