import random
import string 


print("Input a password to determine its strength based on its length, use of uppercase and lowercase letters, numbers, and special characters.")

password = input("Enter a password: ")


#password requirements
min_length = 8
uses_upper = any(x.isupper() for x in password)
uses_lower = any(x.islower() for x in password)
uses_num = any(x.isdigit() for x in password)
spchar = ['!', '@', '#', '$','%', '^','&', '*', '(', ')', '<', '>', ',','.','?','/','[',']','{','}','-','_','+','=',':',';']
uses_spchar = any(x in spchar for x in password)



#checking password for requirements
if len(password) > min_length and uses_upper == True and uses_lower == True and uses_num == True and uses_spchar == True:
    print("Your password is strong!")
if len(password) < min_length:
    print("Password is not 8 characters.")
if uses_upper == False:
    print("Password does not include uppercase letters.")
if uses_lower == False:
    print("Password does not include lowercase letters.")
if uses_num == False:
    print("Password does not include numbers.")
if uses_spchar == False:
    print("Password does not include special characters.")
