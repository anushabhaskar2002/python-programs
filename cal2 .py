def add(num1,num2):
    print(num1+num2)
    return
def sub(num1,num2):
    print(num1-num2)
    return
def multiple(num1,num2):
    print(num1*num2)
    return
def devision(num1,num2):
    print(num1/num2)
    return
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.devision")
num1=int(input("enter first value"))
num2=int(input("enter second value"))
choice=int(input("enter choice.1/2/3/4"))
if choice==1:
    add(num1,num2)
elif choice==2:
    sub(num1,num2)
elif choice==3:
    multiple(num1,num2)
elif choice==4:
    devision(num1,num2)
else:
    print ("wrong choice")
