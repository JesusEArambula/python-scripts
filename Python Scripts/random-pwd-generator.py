import random
import string

pwdLength = int(input("Enter password length: "))
components = [string.ascii_letters, string.digits, "!@#$%&"]
chars = []

for clist in components:
    for item in clist:
        chars.append(item)

def generatePassword():
    password = []
    for i in range(pwdLength):
        rchar = random.choice(chars)
        password.append(rchar)
    return "".join(password)

print(generatePassword())