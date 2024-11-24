''' Make a password strength checker that checks the following parameters in a password:
length, uppercase letters, lowercase letters, numbers, special characters, no-common words '''


password = input("Enter your password: ")

commonPass=('Password@1234', '1234', '9876', '0000', 'hello')
count=0 #initially set to 0


#performs checks on each parameter
if len(password)>=8:
    count+=1
if any(char.isupper() for char in password):
    count+=1
if any(char.islower() for char in password):
    count+=1
if any(char.isdigit() for char in password):
    count+=1
if any(char in "!@#$%^&*()_+" for char in password):
    count+=1
if not any(char in password for char in commonPass):
    count+=1


#Classification as veryStrong, strong, medium, weak
if count<=2:
    print(f"Your Password is weak! with a score of {count}")
elif count<=4:
    print(f"Your Password is medium with a score of {count}")
elif count==5:
    print(f"Your Password is secure with a score of {count}")
if count==6:
    print(f"Your Password is very secure with a score of {count}")
else:
    print("Please redo the action")
