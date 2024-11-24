''' Make a password strength checker that checks the following parameters in a password:
length, uppercase letters, lowercase letters, numbers, special characters, no-common words 
also that tells the shortcomings of the password'''


password = input("Enter your password: ")

commonPass=('Password@1234', '1234', '9876', '0000', 'hello', '')
count=0 #initially set to 0
shortcomings=[]


#performs checks on each parameter
if len(password)>=8:
    count+=1
else:
    shortcomings.append("Minimum characters needed:8")
if any(char.isupper() for char in password):
    count+=1
else:
    shortcomings.append("Add one Uppercase Character")
if any(char.islower() for char in password):
    count+=1
else:
    shortcomings.append("Add one LowerCase Character")
if any(char.isdigit() for char in password):
    count+=1
else:
    shortcomings.append("Add one digit")
if any(char in "!@#$%^&*()_+" for char in password):
    count+=1
else:
    shortcomings.append("Add one Unique Character")
if not any(char in password for char in commonPass):
    count+=1
else:
    shortcomings.append("Too easy to guess")


#Classification as veryStrong, strong, medium, weak
if count<=2:
    print(f"Your Password is weak! with a score of {count}")
elif count<=4:
    print(f"Your Password is medium with a score of {count}")
elif count==5:
    print(f"Your Password is secure with a score of {count}")
elif count==6:
    print(f"Your Password is very secure with a score of {count}")

#Shows the list of the changes that you must do to get a secured password
if count!=6:
    print(shortcomings)
