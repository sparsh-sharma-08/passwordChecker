# passwordChecker
This Python program checks the security of your password based on various parameters and provides feedback on how to improve its strength. The program evaluates your password's length, uppercase and lowercase letters, digits, special characters, and checks for common words.

**Features**
1. Password Length: Checks if the password has a minimum length of 8 characters.
2. Uppercase Letters: Ensures the password contains at least one uppercase letter.
3. Lowercase Letters: Ensures the password contains at least one lowercase letter.
4. Digits: Ensures the password contains at least one numeric character.
5. Special Characters: Ensures the password contains at least one special character from the set !@#$%^&*()_+.
6.No Common Passwords: Checks if the password matches any common passwords (e.g., "Password1234", "1234").
7. Shortcomings Feedback: Provides feedback on missing elements and suggestions for improving the password.

**How it Works**
-> Input: The program prompts the user to enter a password.
-> Evaluation: It evaluates the password based on several security parameters.
-> Score: The program gives a security score based on the number of passed checks:
  Score 6: Very secure password
  Score 5: Secure password
  Score 4: Medium security
  Score 0-3: Weak password
  
**Feedback:** If the password does not meet all the required checks, the program displays a list of shortcomings, highlighting what the user should add or improve to make the password stronger.

**Future Work**
- Allow users to customize the list of common passwords.
- Provide more detailed explanations of the security levels.
- Implement password strength analysis using machine learning or other advanced techniques.
