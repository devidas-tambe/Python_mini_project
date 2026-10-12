# Expence tracker priject
expenses_list=[]

print("<--- Welcome to Expenses Tracker --->")

while True:
    print("=== MENU ===")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

# Add Expense
    if(choice==1):
        date= input("kis date par Kharcha kiya = ")
        category= input("kis type ka charcha kiya = ")
        description=input("Description about kharcha = ")
        amount=float(input("Enter the amount = "))

        expenses={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses_list.append(expenses)
        print("\nDone bro. Expences is added succesfully")

#2. VIEW ALL EXPENSES
    if(choice == 2):
        if(len(expenses_list)==0):
            print("No expenses Added")
        else:
            print("<--- This is your all expenses --->")
            count=1
            for eachkharcha in expenses_list:
                print("kharcha no =",count,"-->", {eachkharcha["date"]},{eachkharcha["category"]},{eachkharcha["description"]},{eachkharcha["amount"]})
                count=count+1

#3. View Total Spending
    elif(choice==3):
        total=0
        for eachkharcha in expenses_list:
            total=total+eachkharcha["amount"]
        print("\nTOTAL KHARCHA = ",total)

#4. EXIT
    elif(choice==4):
        print("Thank You For Using Our System")
        break
    else:
        print("INVALID CHOICE. PLEASE TRY AGAIN")