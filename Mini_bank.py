print("""
1.deposite
2.withdraw
3.Balance check
4.exit
      """)
acc=0
while True:
  choise=input("enter your choice =")
  if choise =="1":
    dep=int(input("enter amount = "))
    print()
    if dep>0:
      acc+=dep
      print("deposite succesfully")
      print("total amountis ",acc)
      print()
    else:
      print("invalid amount please enter positive number")

  elif choise=="2":
    withdraw=int(input("enter withdraw amount :"))
    if withdraw>0:
      if withdraw<acc:
        acc=acc-withdraw
        print(withdraw,"Rs are withdraw")
        print("current amount is :",acc)
        print()
      else:
        print("insufficient balance")
        print()
    else:
      print("negative number not allowed please enter valid amount...")
      print()

  elif choise == "3":
    print("your current amount is ", acc)
    print()

  elif choise=="4":
    print("thank you..")
    break
  
  else:
    print("""
    please choise from 
    1
    2
    3
    4
  """)
  