import random
import string

lenght=int(input("Enter the lenght of the Password:"))
lower= string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols= "!@#$%^&*"

all=lower+upper+num+symbols
temp= random.sample(all,lenght)
password = "".join(temp)
print("The Password is:",password)