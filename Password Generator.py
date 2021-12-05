# PASSWORD GENERATOR
import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*()-+?")
#print(characters)
def Password_Generator():
	user=int(input("Enter Password Length: "))
	random.shuffle(characters)
	password=[]
	for i in range(user):
		password.append(random.choice(characters))
		
	random.shuffle(password)
	
	print("".join(password))
	
Password_Generator()