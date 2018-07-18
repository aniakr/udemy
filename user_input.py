act_password = "12345"

user_password=''
while user_password!=act_password:
    user_password = input("Enter 5 digit password: ")
    if user_password==act_password:
        print ('Password correct')
    else:
        print ("Incorrect password")



