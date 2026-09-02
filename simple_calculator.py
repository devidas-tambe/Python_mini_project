def add(num1,num2): 
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def Devision(num1,num2):
    return num1/num2
    
print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Devision")

user=int(input("Enter the your choise :"))
if user >=5:
    print("invalid input...")
else:
    num1=int(input("Enter the First Number : "))
    num2=int(input("Enter the second Number"))

if user==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif user==2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif user==3:
    print(num1,"x",num2,"=",multiply(num1,num2))
elif user==4:
    print(num1,"/",num2,"=",Devision(num1,num2))
else:
    print("Please try again..")
