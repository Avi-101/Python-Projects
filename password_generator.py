import random
import string

def generate_password():
#Password consists of letters, numbers, and special characters
    includes = string.ascii_letters + string.digits + string.punctuation
    
#Randomly chooses a length of 8-12
    length = random.randint(8, 12)
    
#Use random.choices to select random characters
    password = ''.join(random.choices(includes, k=length))
    
    return password


if __name__ == "__main__":
    print("Here is a randomly generated password: ", generate_password())
