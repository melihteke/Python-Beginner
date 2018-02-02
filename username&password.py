typed_username=input("Please enter your Username\n\n")
typed_pass=input("Please enter your 4 digit code\n\n")

database_password = "1234"
database_username = "kemal"

if typed_username != database_username or typed_pass != database_username:
    print("Wrong username or password, please try again.\n")
else:
    print("Congratulations!!, Now you are authrized to have access\n\n")
