password = 123456
name=input("Enter name: ")
surname = input("Enter surname: ")
guess = input("Enter your passcode: ")

while int(guess)!=password:
    guess = input("Wrong password! Try again: ")
print("Hi %s %s, you're logged in" % (name, surname))

# HOW TO TEST THIS
def password_checker(password, guess):
    while int(guess)!=password:
        print("Incorrect passcode")
        guess = input("Enter your passcode: ")
    print("Correct!")


