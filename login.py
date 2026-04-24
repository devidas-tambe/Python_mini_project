user_name="Shubham_Kotme"
password="Shubham@123"

user=input("Enter the user name : ")
pas=input("Enter the password : ")

if user_name==user:
    if password==pas:
        print("login succesfully...")
    else:
        print("wrong password")
        print("Please try again")
else:
    print("invali username ....")
