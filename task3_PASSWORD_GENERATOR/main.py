import string
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
import random
while True:
    try:
        passwordLength = int(input("Enter password length: "))
        break
    except ValueError:# if the input is not an integer
        print("Enter a valid number")
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("Your password is: ")
password = ""
for i in range(passwordLength):
    password += random.choice(s)

print(password)
