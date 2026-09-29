# rent calculator
rent=int(input("enter the your rent:"))
Food=int(input("enter the cost of food:"))

electricity=int(input("enter the total unit of electricity :"))
charge_per_unit=int(input("Enter the unit rate per unit :"))
total_lightbill = electricity * charge_per_unit

total=rent + Food + total_lightbill
print(total)
student=int(input("enter the number of student :"))


output= (rent + Food + total_lightbill)// student

print("total amount to pay each student: ",output)
