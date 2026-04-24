import random

item_list=["Stone","Paper","Scissor"]
user_choise=input("enter the your choise(stone,paper,scissor) = ")
computer_choise=(random.choice(item_list))

print(f"user choise={user_choise},computer choise ={computer_choise}")


if(user_choise==computer_choise):
    print("Both choose the same= Match tie")

elif (user_choise=="Stone"):
    if(computer_choise=="Paper"):
        print("Computer Win....")
    elif(computer_choise=="Scissor"):
        print("you win....")

elif(user_choise=="Paper"):
    if(computer_choise=="Stone"):
        print("you win....")
    elif(computer_choise=="Scissor"):
        print("Computer win....")

elif(user_choise=="Scissor"):
    if(computer_choise=="Stone"):
        print("Computer win...")
    elif(computer_choise=="Paper"):
        print("you win...")

